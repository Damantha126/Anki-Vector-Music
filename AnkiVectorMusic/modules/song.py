# AnkiVectorMusic (Telegram bot project )
# Copyright (C) 2021  Damantha_Jasinghe

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from __future__ import unicode_literals

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import youtube_dl
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos

from AnkiVectorMusic.config import DURATION_LIMIT
from AnkiVectorMusic.modules.play import arq

@Client.on_message(filters.command("saavn") & ~filters.edited)
async def jssong(_, message):
    global is_downloading
    if len(message.command) < 2:
        await message.reply_text("/saavn requires an argument.")
        return
    if is_downloading:
        await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
        return
    is_downloading = True
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching...")
    try:
        songs = await arq.saavn(query)
        if not songs.ok:
            await message.reply_text(songs.result)
            return
        sname = songs.result[0].song
        slink = songs.result[0].media_url
        ssingers = songs.result[0].singers
        await m.edit("Downloading")
        song = await download_song(slink)
        await m.edit("Uploading")
        await message.reply_audio(audio=song, title=sname, performer=ssingers)
        os.remove(song)
        await m.delete()
    except Exception as e:
        is_downloading = False
        await m.edit(str(e))
        return
    is_downloading = False


# Deezer Music


@Client.on_message(filters.command("deezer") & ~filters.edited)
async def deezsong(_, message):
    global is_downloading
    if len(message.command) < 2:
        await message.reply_text("/deezer requires an argument.")
        return
    if is_downloading:
        await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
        return
    is_downloading = True
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching...")
    try:
        songs = await arq.deezer(query, 1)
        if not songs.ok:
            await message.reply_text(songs.result)
            return
        title = songs.result[0].title
        url = songs.result[0].url
        artist = songs.result[0].artist
        await m.edit("Downloading...")
        song = await download_song(url)
        await m.edit("Uploading...")
        await message.reply_audio(audio=song, title=title, performer=artist)
        os.remove(song)
        await m.delete()
    except Exception as e:
        is_downloading = False
        await m.edit(str(e))
        return
    is_downloading = False
