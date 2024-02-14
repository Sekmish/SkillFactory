import telebot
from bs4 import BeautifulSoup

from config import TOKEN
from extensions import CurrencyConverter, APIException
import requests


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    instructions = "Привет! Я бот для конвертации валют.\n\n" \
                   "Для получения цены на валюту используйте команду в формате:\n" \
                   "<валюта, цену которой хотите узнать> <валюта, в которой надо узнать цену первой валюты> <количество первой валюты>\n" \
                   "Например: USD RUB 100\n\n" \
                   "Для получения списка доступных валют используйте команду /values.\n\n" \
                   "Для получения учетных цен на драгоценные металлы используйте команду /metal\n\n" \
                   "Для получения информации об инфляции используйте команду /inflation"
    bot.reply_to(message, instructions)

@bot.message_handler(commands=['values'])
def handle_values(message):
    values = "Список доступных валют:\n" \
             "- USD (Доллар США)\n" \
             "- EUR (Евро)\n" \
             "- CNY (Китайский юань)\n" \
             "- RUB (Российский рубль)"
    bot.reply_to(message, values)


@bot.message_handler(commands=['inflation'])
def handle_inflation(message):
    try:
        base = 'https://cbr.ru/key-indicators'
        html = requests.get(base).content
        soup = BeautifulSoup(html, 'lxml')

        deno_list = soup.find_all('div', class_='denotement')
        span = soup.find_all('div', class_='value')

        inflation_data = [(deno.text.strip(), span.text.strip()) for deno, span in zip(deno_list[:2], span[:2])]
        response = "ИНФЛЯЦИЯ\n"
        for deno_text, span_text in inflation_data:
            response += f"{deno_text}: {span_text}\n"

        response += "\nКЛЮЧЕВАЯ СТАВКА\n"
        key_rate_data = [(deno.text.strip(), span.text.strip()) for deno, span in zip(deno_list[2:], span[2:])]
        for deno_text, span_text in key_rate_data:
            response += f"{deno_text}: {span_text}\n"

        bot.reply_to(message, response)
    except Exception as e:
        error = f"Произошла ошибка при получении данных о ключевых показателях: {e}"
        bot.reply_to(message, error)

@bot.message_handler(commands=['metal'])
def handle_metal(message):
    try:
        base = 'https://cbr.ru/key-indicators'
        html = requests.get(base).content
        soup = BeautifulSoup(html, 'lxml')

        metal_list = soup.find_all('div', class_='col-md-5')
        price_list = soup.find_all('td', class_='value td-w-4 _bold _end mono-num')
        date_price = soup.find_all('td', class_='value td-w-4 _end')

        response = f"Данные предоставлены на {date_price[0].text}\n"
        metall_data = [(metal.text.strip(), price.text.strip()) for metal, price in zip(metal_list[6:], price_list[3:])]
        for metal_text, price_text in metall_data:
            response += f"{metal_text}: {price_text} руб.\n"

        bot.reply_to(message, response)
    except Exception as e:
        error = f"Произошла ошибка при получении данных о драгоценных металлах: {e}"
        bot.reply_to(message, error)


@bot.message_handler(func=lambda message: True)
def handle_conversion(message):
    try:
        base, quote, amount = message.text.split()
        price = CurrencyConverter.get_price(base.upper(), quote.upper(), float(amount))
        response = "Цена {} {} в {}: {:.2f}".format(amount, base.upper(), quote.upper(), price)
        bot.reply_to(message, response)
    except ValueError:
        error = "Неверный формат команды. Пожалуйста, введите валюты и количество валюты в правильном формате."
        bot.reply_to(message, error)
    except APIException as e:
        bot.reply_to(message, f"Ошибка при получении данных от API: {e}")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")


bot.polling()
