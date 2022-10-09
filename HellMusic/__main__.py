import sys
import asyncio
from config import Config
from pyrogram import idle
from HellMusic.core.logging import LOGS
from HellMusic.helpers.text import DEPLOYED
from HellMusic.core.plugins import load_plugins
from HellMusic import bot, hell, client, helldb, __version__


async def startup():
    if not Config.HELLBOT_SESSION:
        LOGS.error("[HELLBOT_SESSION]: Not a valid session!")
        sys.exit()

    try:
        LOGS.info("••• Music Bot Startup •••")
        await bot.start()
        await client.start()
        await hell.start()
        await load_plugins()
        if Config.DB_URI:
            LOGS.info("••• Database Url Found •••")
            await helldb.get_db()
        LOGS.info(DEPLOYED.format(__version__.version))
        await idle()
    except Exception as e:
        LOGS.error(str(e))


client.loop.run_until_complete(startup())

if len(sys.argv) not in (1, 3, 4):
    client.disconnect()
else:
    try:
        client.run_until_disconnected()
    except ConnectionError:
        pass
