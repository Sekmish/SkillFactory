import requests

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        if base == 'RUB':
            base_value = 1
        else:
            base_value = CurrencyConverter.get_currency_value(base)

        if quote == 'RUB':
            quote_value = 1
        else:
            quote_value = CurrencyConverter.get_currency_value(quote)

        result = round((amount * base_value) / quote_value, 2)
        return result

    @staticmethod
    def get_currency_value(currency):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()

        if 'Valute' not in data:
            raise APIException("Ошибка при получении данных о курсах валют")

        currency_data = data['Valute'].get(currency.upper())

        if not currency_data:
            raise APIException(f"Валюта {currency} не найдена")

        return currency_data['Value']

