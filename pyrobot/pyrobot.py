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

__version__ = "1.0.1"

from pyrogram import Client

from .config import Config


class PyroBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()

        plugins = dict(root=f"{name}/plugins")
        super().__init__(
            session_name=":memory:",
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workdir=Config.WORK_DIR,
            app_version=f"PyroBot v{__version__}",
            workers=8,
            plugins=plugins,
        )

    async def start(self):
        await super().start()
        print(f"PyroBot started with Version v{__version__}")

    async def stop(self, *args):
        await super().stop()
        print("PyroBot stopped. Bye.")
