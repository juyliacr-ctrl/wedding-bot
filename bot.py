import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import ContentTypeFilter

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

if TOKEN is None:
     raise Exception("BOT_TOKEN not found in environment variables")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(ContentTypeFilter(types.ContentType.PHOTO))
async def handle_photo(message: types.Message):
     photo = message.photo[-1]
     caption = f"Фото від @{message.from_user.username or message.from_user.full_name}"
     await bot.send_photo(chat_id=CHAT_ID, photo=photo.file_id, caption=caption)

async def main():
    print("Бот запущений, очікую фото...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
