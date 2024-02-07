"""
1.- Queremos hacer una aplicación que sea capaz de convertir una cantidad de dinero en una moneda a otra moneda, para
ello haremos uso de la API descrita aquí.

Al usuario/a le pediremos:

La moneda desde la que queremos la conversión.
La moneda a la que queremos convertir.
La cantidad de dinero que tenemos.
A tener en cuenta:

Si la consulta da un error hay que indicarlo.
Al usuario se le mostrarán las diferentes unidades de moneda antes de pedir los datos, estas se pueden obtener mediante
consulta en esta misma API.
"""

import requests

KEY_API = '62d2fc1169990d7150f17245'
URL_API = 'https://v6.exchangerate-api.com/v6/'
CONVERT = '/pair/'


def get_all_currencies():
    url = URL_API + KEY_API + '/codes'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['supported_codes']
    else:
        return None


def get_exchange_rate(currency_from, currency_to):
    url = URL_API + KEY_API + CONVERT + currency_from + '/' + currency_to
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['conversion_rate']
    else:
        return None


def convert_currency(currency_from, currency_to, amount):
    exchange_rate = get_exchange_rate(currency_from, currency_to)
    if exchange_rate is None:
        return None
    else:
        return amount * exchange_rate


def main():
    currencies = get_all_currencies()
    if currencies is None:
        print('Error al obtener las monedas')
        return
    print('Monedas disponibles:')
    for currency in currencies:
        print(currency)
    currency_from = input('Introduce la moneda desde la que quieres convertir: ')
    currency_to = input('Introduce la moneda a la que quieres convertir: ')
    amount = float(input('Introduce la cantidad de dinero que quieres convertir: '))
    result = convert_currency(currency_from, currency_to, amount)
    if result is None:
        print('Error al obtener el tipo de cambio')
    else:
        print(f'{amount:.2f} {currency_from} son {result:.2f} {currency_to}')


if __name__ == '__main__':
    main()
