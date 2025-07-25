from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import F
import asyncio
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = -1002752004418

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
      await message.answer("Привіт! Надішли фото — я перекину в загальний чат ")

@dp.message(F.photo)
async def handle_photo(message: Message):
      photo = message.photo[-1]
      caption = message.caption or ""
      await bot.send_photo(chat_id=GROUP_ID, photo=photo.file_id, caption=caption)

async def main():
      logging.basicConfig(level=logging.INFO)
      await dp.start_polling(bot)

if __name__ == "__main__":
      asyncio.run(main())
