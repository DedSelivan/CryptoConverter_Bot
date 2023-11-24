import requests
import json
from config import keys_crypto, keys_money


# Создаём класс для отлова ошибок пользователя
class ConvertionExemption(Exception):
    pass

# Создаём класс с одним статическим методом, который будет производить конвертацию криптовалюты. В качестве параметров
# передаем данные введённые пользователем
class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        try:
            base_ticker = keys_crypto[base]
        except KeyError:
            raise ConvertionExemption(f'Не удалось обработать валюту {base}')
        try:
            quote_ticker = keys_money[quote]
        except KeyError:
            raise ConvertionExemption(f'Не удалось обработать валюту {quote}')
        try:
            amount = float(amount)
        except KeyError:
            raise ConvertionExemption(f'Не удалось обработать количество: {amount}')

        request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        response = json.loads(request.content)[keys_money[quote]]

        return response
