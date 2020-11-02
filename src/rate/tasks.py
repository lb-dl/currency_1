from bs4 import BeautifulSoup

from celery import shared_task

from rate import choices
from rate.utils import to_decimal

import requests


@shared_task
def parse_privatbank():
    from rate.models import Rate
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    # rase an error if status is not 200
    response.raise_for_status()
    data = response.json()
    source = choices.SOURCE_PRIVATBANK
    currency_map = {
        'USD': choices.CURRENCY_USD,
        'EUR': choices.CURRENCY_EUR,
    }
    for row in data:
        if row['ccy'] in currency_map:
            buy = to_decimal(row['buy'])
            sale = to_decimal(row['sale'])
            currency = currency_map[row['ccy']]
            last_rate = Rate.objects.filter(source=source, currency=currency).last()
            if last_rate is None or buy != last_rate.buy or sale != last_rate.sale:
                Rate.objects.create(
                    currency=currency,
                    source=source,
                    sale=sale,
                    buy=buy
                )


@shared_task
def parse_monobank():
    from rate.models import Rate
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()[0:2]
    source = choices.SOURCE_MONOBANK
    currency_map = {
        840: choices.CURRENCY_USD,
        978: choices.CURRENCY_EUR,
    }
    for row in data:
        if row['currencyCodeA'] in currency_map:
            buy = to_decimal(row['rateBuy'])
            sale = to_decimal(row['rateSell'])
            currency = currency_map[row['currencyCodeA']]
            last_rate = Rate.objects.filter(source=source, currency=currency).last()
            if last_rate is None or buy != last_rate.buy or sale != last_rate.sale:
                Rate.objects.create(
                    currency=currency,
                    source=source,
                    sale=sale,
                    buy=buy
                )


@shared_task
def parse_minora():
    from rate.models import Rate
    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    source = choices.SOURCE_MINORA
    currency_map = {
        'Dollar': choices.CURRENCY_USD,
        'Euro': choices.CURRENCY_EUR,
    }
    for key in data:
        if key in currency_map:
            currency = currency_map[key]
            buy = to_decimal(data[key]['buy'])
            sale = to_decimal(data[key]['sale'])
            last_rate = Rate.objects.filter(source=source, currency=currency).last()
            if last_rate is None or buy != last_rate.buy or sale != last_rate.sale:
                Rate.objects.create(
                    currency=currency,
                    source=source,
                    buy=buy,
                    sale=sale)


@shared_task
def parse_pumb():
    from rate.models import Rate
    url = 'https://retail.pumb.ua/'
    response = requests.get(url)
    response.raise_for_status()
    source = choices.SOURCE_PUMB
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find('table')
    buy_usd = table.find_all('tr')[1].find_all('td')[1].text
    sale_usd = table.find_all('tr')[1].find_all('td')[2].text
    buy_euro = table.find_all('tr')[2].find_all('td')[1].text
    sale_euro = table.find_all('tr')[2].find_all('td')[2].text
    usd = dict(ccy='USD', buy=buy_usd, sale=sale_usd)
    euro = dict(ccy='EUR', buy=buy_euro, sale=sale_euro)
    data = [usd, euro]
    currency_map = {
        'USD': choices.CURRENCY_USD,
        'EUR': choices.CURRENCY_EUR,
    }
    for row in data:
        if row['ccy'] in currency_map:
            buy = to_decimal(row['buy'])
            sale = to_decimal(row['sale'])
            currency = currency_map[row['ccy']]
            last_rate = Rate.objects.filter(source=source, currency=currency).last()
            if last_rate is None or buy != last_rate.buy or sale != last_rate.sale:
                Rate.objects.create(
                    currency=currency,
                    source=source,
                    sale=sale,
                    buy=buy
                )


@shared_task
def parse_kredobank():
    from rate.models import Rate
    url = 'https://kredobank.com.ua/info/kursy-valyut/commercial'
    response = requests.get(url)
    response.raise_for_status()
    source = choices.SOURCE_KREDOBANK
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find('table')
    buy_usd = int(table.find_all('tr')[1].find_all('td')[3].text)/100
    sale_usd = int(table.find_all('tr')[1].find_all('td')[2].text)/100
    buy_euro = int(table.find_all('tr')[2].find_all('td')[3].text)/100
    sale_euro = int(table.find_all('tr')[2].find_all('td')[2].text)/100
    usd = dict(ccy='USD', buy=buy_usd, sale=sale_usd)
    euro = dict(ccy='EUR', buy=buy_euro, sale=sale_euro)
    data = [usd, euro]
    currency_map = {
        'USD': choices.CURRENCY_USD,
        'EUR': choices.CURRENCY_EUR,
    }
    for row in data:
        if row['ccy'] in currency_map:
            buy = to_decimal(row['buy'])
            sale = to_decimal(row['sale'])
            currency = currency_map[row['ccy']]
            last_rate = Rate.objects.filter(source=source, currency=currency).last()
            if last_rate is None or buy != last_rate.buy or sale != last_rate.sale:
                Rate.objects.create(
                    currency=currency,
                    source=source,
                    sale=sale,
                    buy=buy
                )
