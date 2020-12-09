import django_filters
from django_filters import DateRangeFilter

from rate.models import Rate


class RateFilter(django_filters.FilterSet):

    date_range = DateRangeFilter(field_name='created')

    class Meta:
        model = Rate
        fields = ['source', 'currency']
