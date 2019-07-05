import requests
respForm = {'format': 'json'}

print('exchange rate PLN -> foreign currency')
currencyCode = input('type in currency code: ')

requestFromNBP = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/' + currencyCode + '/today/', params=respForm)

print(requestFromNBP.status_code)

if requestFromNBP.status_code == 404:
    print('currency not found')
else:
    zl = input('type in money amount in PLN: ')
    response = requestFromNBP.json()
    print(response)

    foreignCurrency_lvl1 = response['rates'][0]
    foreignCurrency_lvl2 = foreignCurrency_lvl1['mid']

    amountExchange = round(float(float(zl)/foreignCurrency_lvl2), 2)
    print(str(zl) + ' PLN is ' + str(amountExchange) + ' ' + currencyCode)
