import requests

respForm = {'format': 'json'}

print('exchange rate PLN -> CHF')
zl = input('type in money amount in PLN: ')
requestFromNBP = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/CHF/today/', params = respForm)

print(requestFromNBP.status_code)
response = requestFromNBP.json()
print(response)

foreignCurrency_lvl1 = response['rates'][0]
foreignCurrency_lvl2 = foreignCurrency_lvl1['mid']

amountExchange = round(float(foreignCurrency_lvl2)*float(zl),2)
print(str(zl) + 'zl wynosi ' + str(amountExchange) + ' CHF')