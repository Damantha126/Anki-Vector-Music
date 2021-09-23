"""
Anki Vector Music- Telegram bot project
Copyright (C) 2021  Damantha Jasinghe
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
Modified by Damantha Jasinghe
"""

import requests
from pyrogram import Client as Bot

from AnkiVectorMusic.config import API_HASH
from AnkiVectorMusic.config import API_ID
from AnkiVectorMusic.config import BG_IMAGE
from AnkiVectorMusic.config import BOT_TOKEN
from AnkiVectorMusic.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AnkiVectorMusic.modules"),
)

bot.start()
run()
