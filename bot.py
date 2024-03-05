import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers.buy_cmd_handler import buy_router
from handlers.start_cmd_handler import start_router
from handlers.tech_support_cmd_handler import tech_router

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        start_router,
        tech_router,
        buy_router,
    )

    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
