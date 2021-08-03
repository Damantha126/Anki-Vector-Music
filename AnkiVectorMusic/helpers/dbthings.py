import os
import time
import string
import random
import datetime
import aiofiles
import asyncio
import traceback
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

from AnkiVectorMusic.helpers.database import db, Database, dcmdb
from AnkiVectorMusic.config import LOG_CHANNEL, BROADCAST_AS_COPY

async def handle_user_status(bot, cmd):
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"**📢 News ** \n#New_USER **Started To Using Meh!** \n\nFirst Name: `{cmd.from_user.first_name}` \nUser ID: `{cmd.from_user.id}` \nProfile Link: [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})"
        )

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
                datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("Sorry To Say! but **You are banned** 😂! Ask in **@TheAnkiVectorbot** if you think this was an mistake.", quote=True)
            return
    await cmd.continue_propagation()
    
    
    
# Broadcast Things

broadcast_ids = {}


async def send_msg(user_id, message):
    try:
        if BROADCAST_AS_COPY is False:
            await message.forward(chat_id=user_id)
        elif BROADCAST_AS_COPY is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


async def main_broadcast_handler(m, db):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=f"**Broadcasting has Started !** You'll be notified with logs after finishing 😁!"
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast-logs.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"Broadcasting Completed ✅! \n**Completed In:** `{completed_in}` \n\n**Total Users:** `{total_users}` \n**Total Done:** `{done}` \n**Total Success:** `{success}` \n**Total Failed:** `{failed}`",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast-logs.txt',
            caption=f"Broadcasting Completed ✅! \n**Completed In:** `{completed_in}`\n\n**Total Users:** `{total_users}` \n**Total Done:** `{done}` \n**Total Success:** `{success}` \n**Total Failed:** `{failed}`",
            quote=True
        )
    os.remove('broadcast-logs.txt')



# Anti Command Feature

delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool:
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    if not chat:
        return True
    return False


async def delcmd_on(chat_id: int):
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int):
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})
