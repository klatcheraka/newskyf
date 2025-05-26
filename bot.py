import subprocess
import sys

print("Python executable:", sys.executable)

# Проверяем версию pip
pip_version = subprocess.run(["pip", "--version"], capture_output=True, text=True)
print("Pip version:", pip_version.stdout)

# Список установленных пакетов
pip_list = subprocess.run(["pip", "list"], capture_output=True, text=True)
print("Installed packages:\n", pip_list.stdout)

# Основной код
from telegram import Bot

import os

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("Ошибка: не найден токен в переменных окружения.")
    sys.exit(1)

bot = Bot(token=TOKEN)

try:
    me = bot.get_me()
    print(f"✅ Токен рабочий! Бот: @{me.username}, ID: {me.id}")
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
