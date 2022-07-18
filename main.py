from forex_python.converter import CurrencyRates

cr = CurrencyRates()

amount = int(input('What amount do you wanna convert today? '))
from_currrency = input("Please enter the currency code that has to be converted: ").upper()
to_currency = input("Please enter the currency code to convert: ").upper()
print(f'You are converting {amount} {from_currrency} to {to_currency}')
output = cr.convert(from_currrency, to_currency, amount)
print('The converted amount is:', output)
