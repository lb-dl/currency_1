from rate.api.serializers import RateSerializer
from rate.models import Rate

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class RateAPIViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-id')
    serializer_class = RateSerializer
    pagination_class = PageNumberPagination
