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

import os
from AnkiVectorMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!\n I can play music in voice chats of Telegeam Groups & Channels.\nI have a lot of cool feature that will amaze you!\n\nTo add in your group contact us at @ankivectorUpdates .\n\nHit /help list of available commands. **"
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}
\n\n♦️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats
\n♦️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**⏺Setting up⏺**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry
**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
**Commands**
**⏺Song Playing⏺**

- /play: Play song using youtube music
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
**=>> Playback ⏯**
- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist
*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        
f"""
**⏺Channel Music Play⏺**
\n\n <b>♦️ For linked group admins only:</b>

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat
channel is also can be used instead of c ( /cplay = /channelplay )
\n\n♦️ If you donlt like to play in linked group:
\n1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**⏺More tools⏺**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
"""
      ]
