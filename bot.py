import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL = os.getenv("CHANNEL")

if not TOKEN:
    raise ValueError("Отсутствует TOKEN! Добавь переменную окружения TOKEN.")

bot = Bot(token=TOKEN)

def main():
    try:
        me = bot.get_me()
        print(f"✅ Бот @{me.username} запущен успешно!")
        # Здесь можно добавить остальной функционал бота
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")

if __name__ == "__main__":
    main()
