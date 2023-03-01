import requests, time, openpyxl


#  URL путь на json файл с данными
url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

#  Заголовки запроса
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

#  Дополнительные параметры запроса
params = {
    "proMerchantAds": False,
    "page": 1,
    "rows": 10,
    "payTypes": ["TinkoffNew"],
    "countries": [],
    "publisherType": None,
    "transAmount": "",
    "asset": "USDT",
    "fiat": "RUB",
    "tradeType": "BUY"
}

"""
    ПРОГРАММА РАБОТАЕТ ПОКА ЕЁ ПРИНУДИТЕЛЬНО НЕ ЗАВЕРШАТ СОЧЕТАНИЕМ КЛАВИШ Ctrl + C, С ПЕРЕРЫВОМ 1 минуту !!!
"""
while True:

    # Запрос данных
    response = requests.post(
        url=url,
        headers=headers,
        json=params
    ).json()

    """
        Открытие существующего экзель файла и получение ссылки на нужную страницу
        ИЛИ
        Создание нового с настройкой.
    """
    try:
        book = openpyxl.load_workbook(filename='data.xlsx')  # Открытие существующего экзель файла
        sheet = book['Prices']  # Получение ссылки на нужную страницу файла или "книги"
    except:
        book = openpyxl.Workbook()  # Создание нового экзель объекта или "книги"
        book.remove(book.active)  # Удаление страниц, созданных по умолчанию
        sheet = book.create_sheet('Prices')  # Создание страницы с ценами

        # Создание заголовков для колонок
        sheet.insert_rows(0)
        sheet['A1'] = 'Дата'
        sheet['B1'] = 'nickName'
        sheet['C1'] = 'Цена'

    # Создание ссылок на распарсеные данные
    date_and_time = time.strftime('%d.%m.%Y %H:%M')
    nickName = response['data'][0]['advertiser']['nickName']
    price = response['data'][0]['adv']['price']
    row = [
        date_and_time,
        nickName,
        price
    ]
    # Добавление данных в страницу
    sheet.append(row)

    # Сохранение файла
    book.save('data.xlsx')

    # Перерыв 1 минута
    time.sleep(60)
