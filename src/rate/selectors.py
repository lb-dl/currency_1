from django.core.cache import cache

from rate import choices
from rate.models import Rate


def get_latest_rates():
    rates = []
    key = Rate.cache_key()
    if key in cache:
        return cache.get(key)
    else:
        for source_int, source_str in choices.SOURCE_CHOICES:
            for currency_int, _ in choices.CURRENCY_CHOICES:
                rate = Rate.objects\
                    .filter(source=source_int, currency=currency_int) \
                    .order_by('created') \
                    .last()
                if rate:
                    rates.append(rate)
    cache.set('key', rates)
    return rates
