from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from rate import choices
from rate.models import Rate
from rate.utils import to_decimal

import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        date_format = '%d.%m.%Y'
        created = datetime(2018, 1, 1)
        end = datetime.now()
        date_generated = [
            created + timedelta(days=x)
            for x in range(8, (end-created).days)
        ]
        for created in date_generated:
            created_str = created.strftime(date_format)
            url = 'https://api.privatbank.ua/p24api/exchange_rates'
            params = {'json': '', 'date': created_str}
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            exchangeRate = data['exchangeRate']
            source = choices.SOURCE_PRIVATBANK
            currency_map = {
                'USD': choices.CURRENCY_USD,
                'EUR': choices.CURRENCY_EUR,
            }
            for row in exchangeRate:
                if row['currency'] in currency_map:
                    buy = to_decimal(row['purchaseRate'])
                    sale = to_decimal(row['saleRate'])
                    currency = currency_map[row['currency']]
                    last_rate = Rate.objects.filter(
                        source=source,
                        currency=currency,
                        created=created,
                    ).last()
                    if last_rate is None:
                        rate = Rate.objects.create(
                            currency=currency,
                            source=source,
                            sale=sale,
                            buy=buy,
                        )
                        rate.created = created
                        rate.save(update_fields=('created',))
