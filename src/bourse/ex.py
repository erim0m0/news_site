# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://sourcearena.ir/api/?token={}&crypto_v2=btc'
# my_token = '44165d000a589b75bee65a32154d0412'
# result = requests.post(url.format(my_token))
# r = result.json()
# print(r)

# 8Wk5NWWQqi0gNPfcNanJGp87CetPdFPf

import requests

payload = {}
headers = {
    "apikey": "8Wk5NWWQqi0gNPfcNanJGp87CetPdFPf"
}

url = ["https://api.apilayer.com/currency_data/live?source=EUR&currencies=USD",
       "https://api.apilayer.com/currency_data/live?source=GBP&currencies=USD"]

for source in range(1):
    response = requests.request("GET", source, headers=headers, data=payload)
    status_code = response.status_code
    result = response.json()
    print(result)
