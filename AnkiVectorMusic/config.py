# AnkiVectorMusic Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Damantha_Jasinge
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
# Modified by Damantha_Jasinge

import os
from os import getenv

from dotenv import load_dotenv
from helpers.modhelps import fetch_heroku_git_url


if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AnkiVectorUpdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/d42b1a9fcd8f735c4be8b.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AnkivectorMusicbot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AnkiSupport_Official")
PROJECT_NAME = getenv("PROJECT_NAME", "DT Project")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Damantha126/Anki-Vector-Music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
DATABASE_URL = os.environ.get("DATABASE_URL")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
BOT_OWNER = int(os.environ.get("BOT_OWNER"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# Updator Configs
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
U_BRANCH = "master"
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
