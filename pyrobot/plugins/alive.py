# PyroBot - Telegram Userbot powered by Pyrogram
# Copyright (C) 2020 - Nicolas "ColinShark" Neht

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

from ..config import Config


@Client.on_message(filters.command("alive", Config.CMD_HANDLER))
async def alive(_, msg: Message):
    await msg.reply("`I'm alive, Master`")


@Client.on_message(filters.command("ping", Config.CMD_HANDLER))
async def ping_me(_, msg: Message):
    start = datetime.now()
    pong = await msg.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await pong.edit(f"**Pong!**\n`{ms} ms`")
