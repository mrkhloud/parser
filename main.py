import requests
from time import sleep


url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 '
                  '(Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 '
                  '(KHTML, like Gecko) '
                  'Chrome/108.0.0.0 '
                  'YaBrowser/23.1.2.987 '
                  'Yowser/2.5 '
                  'Safari/537.36',
}

params = {
    "proMerchantAds":False,
    "page":1,
    "rows":10,
    "payTypes":["TinkoffNew"],
    "countries":[],
    "publisherType":None,
    "transAmount":"",
    "asset":"USDT",
    "fiat":"RUB",
    "tradeType":"BUY"
}

while True:
    response = requests.post(
        url=url,
        headers=headers,
        json=params
    ).json()
    print(response['data'][0]['advertiser']['nickName'])
    print(response['data'][0]['adv']['price'])
    sleep(60)
