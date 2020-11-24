from unittest.mock import MagicMock

from rate.models import Rate
from rate.tasks import parse_kredobank, parse_minora, parse_monobank, parse_privatbank, parse_pumb


def test_parse_privatbank(mocker):
    count_rates = Rate.objects.count()
    currencies = [{"ccy": "USD", "base_ccy": "UAH", "buy": "28.40000", "sale": "28.80000"},
                  {"ccy": "EUR", "base_ccy": "UAH", "buy": "33.00000", "sale": "33.60000"},
                  {"ccy": "RUR", "base_ccy": "UAH", "buy": "0.35300", "sale": "0.39300"},
                  {"ccy": "BTC", "base_ccy": "USD", "buy": "12854.7271", "sale": "14207.8563"}]
    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = MagicMock(
        status_code=200,
        json=lambda: currencies
    )
    parse_privatbank()
    assert Rate.objects.count() == count_rates + 2

    parse_privatbank()
    assert Rate.objects.count() == count_rates + 2


def test_parse_monobank(mocker):
    count_rates = Rate.objects.count()
    currencies = [
        {'currencyCodeA': 840, 'currencyCodeB': 980, 'date': 1604499607, 'rateBuy': 28.37, 'rateSell': 28.65},
        {'currencyCodeA': 978, 'currencyCodeB': 980, 'date': 1604476207, 'rateBuy': 33.05, 'rateSell': 33.5503}
    ]
    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = MagicMock(
        status_code=200,
        json=lambda: currencies
    )
    parse_monobank()
    assert Rate.objects.count() == count_rates + 2

    parse_monobank()
    assert Rate.objects.count() == count_rates + 2


def test_parse_minora(mocker):
    count_rates = Rate.objects.count()
    currencies = {"Dollar": {"buy": "28.40", "sale": "28.60"},
                  "Euro": {"buy": "33.25", "sale": "33.45"},
                  "Rub": {"buy": "0.353", "sale": "0.362"}
                  }
    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = MagicMock(
        status_code=200,
        json=lambda: currencies
    )
    parse_minora()
    assert Rate.objects.count() == count_rates + 2

    parse_minora()
    assert Rate.objects.count() == count_rates + 2


def test_parse_pumb():
    count_rates = Rate.objects.count()
    parse_pumb()
    assert Rate.objects.count() == count_rates + 2
    parse_pumb()
    assert Rate.objects.count() == count_rates + 2


def test_parse_kredobank():
    count_rates = Rate.objects.count()
    parse_kredobank()
    assert Rate.objects.count() == count_rates + 2
    parse_kredobank()
    assert Rate.objects.count() == count_rates + 2
