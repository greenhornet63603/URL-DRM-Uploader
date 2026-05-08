import asyncio
import logging
import os
import shutil

from pyrogram import Client, raw, types
from typing import Iterable, List, Union

from bot.config import Config
from bot.utils import add_admin, start_webserver, set_commands

import pyromod

logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("apscheduler").setLevel(logging.WARNING)


class Bot(Client):

    def __init__(self):
        super().__init__(
            "bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="bot/plugins"),
        )

    async def start(self):
        await super().start()

        os.makedirs("downloads", exist_ok=True)
        os.makedirs("Videos", exist_ok=True)

        me = await self.get_me()

        self.owner = await self.get_users(
            int(Config.OWNER_ID)
        )

        self.username = f"@{me.username}"

        logging.info("Bot started")
        logging.info(f"Owner: {self.owner.mention}")

        await add_admin(self.owner.id)

        await set_commands(self)

        if Config.WEB_SERVER:
            await start_webserver()

    async def stop(self, *args):
        shutil.rmtree("downloads", ignore_errors=True)
        shutil.rmtree("Videos", ignore_errors=True)

        await super().stop()

    async def get_users(
        self,
        user_ids: Union[int, str, Iterable[Union[int, str]]],
        raise_error: bool = True,
        limit: int = 200,
    ):

        is_iterable = not isinstance(user_ids, (int, str))

        user_ids = (
            list(user_ids)
            if is_iterable
            else [user_ids]
        )

        users = types.List()

        user_ids_chunks = [
            user_ids[i:i + limit]
            for i in range(0, len(user_ids), limit)
        ]

        async def resolve(user_id):
            try:
                return await self.resolve_peer(user_id)

            except Exception:

                if raise_error:
                    raise

                return user_id

        for chunk in user_ids_chunks:

            chunk_resolved = await asyncio.gather(
                *[
                    resolve(i)
                    for i in chunk
                    if i is not None
                ]
            )

            blocked_accounts = [
                i for i in chunk_resolved
                if isinstance(i, int)
            ]

            chunk_resolved = list(
                filter(None, chunk_resolved)
            )

            chunk_resolved = [
                i for i in chunk_resolved
                if not isinstance(i, int)
            ]

            if chunk_resolved:

                r = await self.invoke(
                    raw.functions.users.GetUsers(
                        id=chunk_resolved
                    )
                )

                for i in r:
                    users.append(
                        types.User._parse(self, i)
                    )

            for i in blocked_accounts:
                users.append(i)

        return users if is_iterable else users[0]
