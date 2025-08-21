from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import environ


load_dotenv()

bot = Bot(token=environ.get("TOKEN"))
dp = Dispatcher()