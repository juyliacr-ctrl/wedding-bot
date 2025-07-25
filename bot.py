import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_id = message.photo[-1].file_id
        caption = f"📷 Фото від @{message.from_user.username or message.from_user.first_name}"
        bot.send_photo(chat_id=CHAT_ID, photo=file_id, caption=caption)
    except Exception as e:
        bot.send_message(message.chat.id, "Сталася помилка при пересиланні фото.")

bot.polling(non_stop=True)
