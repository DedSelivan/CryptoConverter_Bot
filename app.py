import telebot
from config import token, keys_crypto, keys_money
from extensions import CurrencyConverter, ConvertionExemption

# Создаём переменную bot , в ней будем хранить наш токен
bot = telebot.TeleBot(token)


# Обработчик команды /start. При вызове выводит приветсвенное сообщение
@bot.message_handler(commands=['start'])
def start_bot(message: telebot.types.Message):
    start_text = (f'Доброго времени суток, дорогой {message.chat.username}!\n\nЯ, бот-конвертер криптовалют. '
                  f'Я умею конвертировать криптовалюту в денежную валюту.\n\n'
                  f'- Команда /help покажет инструкции и команды.\n')

    bot.send_message(message.chat.id, start_text)


# Обработчик команды /help. При вызове показывает инструкции и команды
@bot.message_handler(commands=['help'])
def help_bot(message: telebot.types.Message):
    help_text = (f'Инструкции:\n\n- Чтобы произвести конвертацию, введите боту '
                 f'команду в следующем формате:\n\n<конвертируемая валюта> <валюта в которую конвертируем> '
                 f'<количество конвертируемой валюты>\n\nПРИМЕР: BTC USD 10\n\nКоманды:\n\n/start - запускает бота и '
                 f'выводит приветственное сообщение\n\n/crypto - показывает доступные криптовалюты\n\n/values - '
                 f'показывает доступные валюты')

    bot.send_message(message.chat.id, help_text)


# Обработчик команды /crypto. При вызове показывает доступные криптовалюты
@bot.message_handler(commands=['crypto'])
def crypto_bot(message: telebot.types.Message):
    crypto_text = 'Доступные криптовалюты:\n'
    for key in keys_crypto.keys():
        crypto_text = '\n'.join((crypto_text, key))
    bot.reply_to(message, crypto_text)


# Обработчик команды /values. При вызове показывает доступные валюты
@bot.message_handler(commands=['values'])
def value_bot(message: telebot.types.Message):
    value_text = 'Доступные валюты:\n'
    for key in keys_money.keys():
        value_text = '\n'.join((value_text, key))
    bot.reply_to(message, value_text)


# Обработчик вводимого пользователем сообщения. Пользователь вводит валюты для конвертации и количество и в ответ
# получает сообщение с выполненной конвертацией
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.upper().split(' ')

        if len(values) < 3:
            raise ConvertionExemption('Слишком мало параметров!')
        elif len(values) > 3:
            raise ConvertionExemption('Слишком много параметров!')

        base, quote, amount = values
        result = CurrencyConverter.get_price(base, quote, amount)
    except ConvertionExemption as e:
        bot.reply_to(message, f'Ошибка пользователя!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} равно:  {round(result * (int(amount)), 2)} {quote}'
        bot.send_message(message.chat.id, text)


bot.infinity_polling()
