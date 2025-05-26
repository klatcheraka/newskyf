import os
from telegram import Bot
from telegram.error import TelegramError

def main():
    TOKEN = os.environ.get("TOKEN")
    CHANNEL = os.environ.get("CHANNEL")

    if not TOKEN or not CHANNEL:
        print("❌ Ошибка: не заданы переменные окружения TOKEN или CHANNEL")
        return

    bot = Bot(token=TOKEN)

    try:
        me = bot.get_me()
        print(f"✅ Токен рабочий! Бот: @{me.username}, ID: {me.id}")
        
        # Пример: отправим сообщение в канал
        bot.send_message(chat_id=CHANNEL, text="Бот успешно запущен!")
        print("Сообщение отправлено в канал.")
        
    except TelegramError as e:
        print(f"❌ Ошибка Telegram API: {e}")

if __name__ == "__main__":
    main()
