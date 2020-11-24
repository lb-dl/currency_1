from decimal import Decimal


def display(obj, attr: str):
    get_display = f'get_{attr}_display'
    if hasattr(obj, get_display):
        return getattr(obj, get_display)()
    return getattr(obj, attr)


def to_decimal(num):
    TWOPLACES = Decimal(10) ** -2
    return Decimal(num).quantize(TWOPLACES)
