import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
     raise Exception("BOT_TOKEN або CHAT_ID не знайдено в .env")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(F.photo)
async def handle_photo(message: Message):
     photo = message.photo[-1] # найбільше зображення
     caption = message.caption or ""
     await bot.send_photo(chat_id=CHAT_ID, photo=photo.file_id, caption=caption)
     await message.reply("Фото надіслано в групу 💌")

async def main():
     print("Бот запущений, очікую фото...")
     await dp.start_polling(bot)

if __name__ == "__main__":
     asyncio.run(main())
