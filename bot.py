from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ContentType
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
import asyncio
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.content_type == ContentType.PHOTO)
async def handle_photo(message: Message):
 for photo in message.photo:
 await bot.send_photo(CHAT_ID, photo.file_id, caption=f"Фото від @{message.from_user.username or message.from_user.full_name}")

async def main():
 await dp.start_polling(bot)

if __name__ == "__main__":
 asyncio.run(main())
