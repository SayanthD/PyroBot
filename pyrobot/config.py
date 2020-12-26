# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved

# https://github.com/UsergeTeam/Userge-Assistant/blob/master/assistant/config.py

import os

from pyrogram import filters


class Config:
    APP_ID = int(os.environ.get("APP_ID", 0))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CMD_HANDLER = os.environ.get("CMD_HANDLER", ".")
    WORK_DIR = os.environ.get("WORK_DIR", "./workdir")
    AUTH_CHATS = {os.environ.get("AUTH_CHATS", 0)}
    if os.environ.get("AUTH_CHATS"):
        AUTH_CHATS.update(map(int, os.environ.get("AUTH_CHATS").split()))


auth_chats = filters.chat(list(Config.AUTH_CHATS))
