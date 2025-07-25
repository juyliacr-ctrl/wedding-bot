import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if TOKEN is None:
     raise Exception("BOT_TOKEN not found in environment variables")

if CHAT_ID is None:
     raise Exception("CHAT_ID not found in environment variables")
else:
     CHAT_ID = int(CHAT_ID)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message(F.photo)
async def handle_photo(message: types.Message):
     photo = message.photo[-1]
     caption = f"Фото від @{message.from_user.username or message.from_user.full_name}"
     await bot.send_photo(chat_id=CHAT_ID, photo=photo.file_id, caption=caption)

async def main():
     print("Бот запущений, очікую фото...")
     await dp.start_polling()

if __name__ == "__main__":
     asyncio.run(main())
