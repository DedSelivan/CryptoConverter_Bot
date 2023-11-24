# CryptoConverter_Bot:
Telegram-бот конвертер валют. Бот умеет конвертировать доступные боту криптовалюты в денежную валютую.

API для взятия курса валют: https://www.cryptocompare.com/

# Содержание:
файл app.py - основной файл содержащий обработчики, которые будут выполнять основную часть работы.

файл extensions.py - содержит все классы.

файл config.py - содержит токен для подключения и информацию о доступных валютах и криптовалютах.

Файл requirements.py - содержит использующиеся библиотеки
# Настройка бота:

1. Создаем виртуапльное окружение командой:
    
    python3 -m venv venv
2. Активируем виртуальное окружение командой (MacOS/Linux):

    source venv/bin/activate
   
    для Windows другая команда:
    
    \env\Scripts\activate.bat
3. Установка зависимостей:
    
    pip install -r requirements.txt
4. Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее вертуальное окружение.

# Запуск бота:

Для запуска бота нужно иметь токен от BotFather (Telegram: @BotFather)