from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from config.strings import *
import os
import sys
import asyncio
import logging
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, CommandObject, Command, MagicData
from aiogram import F
from aiogram.types import Message
from aiogram.types import Contact
from config import middleware

# Routers
from config.routers.user_router import *

load_dotenv('./config/.env')

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.update.middleware(
    middleware=middleware.SupabaseMiddleware(
        os.getenv('SUPABASE_URL'),
        os.getenv('SUPABASE_KEY')
    )
)

async def main() -> None:
    dp.include_router(user_router)
    await dp.start_polling(bot, skip_updates=True)