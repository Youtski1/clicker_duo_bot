import asyncio
from .loader import bot, dp
import logging
from aiohttp import ClientSession
from .routers import setup

from .middlewaries import (
    ServicesMiddleware
)


async def main():
    async with ClientSession() as session:
        logging.basicConfig(level=logging.INFO)

        dp.message.middleware(ServicesMiddleware(session=session))
        dp.callback_query.middleware(ServicesMiddleware(session=session))
        setup(dp=dp)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main=main())