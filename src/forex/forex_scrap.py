import requests

payload = {}
headers = {
    "apikey": "8Wk5NWWQqi0gNPfcNanJGp87CetPdFPf"
}

urls = ["https://api.apilayer.com/currency_data/live?source=EUR&currencies=USD",
       "https://api.apilayer.com/currency_data/live?source=GBP&currencies=USD"]

data_list = []

def get_data():
    for url in urls:
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.json().get('quotes')
        for k,v in result.items():
            data_list.append(v)
