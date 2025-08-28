from aiogram import Bot, Dispatcher
from os import environ

bot = Bot(token=environ.get("TOKEN"))
dp = Dispatcher()