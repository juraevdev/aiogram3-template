import logging
import sys
import asyncio
import middlewares, filters, handlers

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.help_command import help_router
from handlers.users.start import start_router
from handlers.users.echo import echo_router
from loader import dp

from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(help_router)
    dp.include_router(start_router)
    dp.include_router(echo_router)

    await dp.start_polling(bot)
    await set_default_commands(bot)
    await on_startup_notify(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
