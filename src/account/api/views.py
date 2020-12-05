from account.api.serializers import AvatarSerializer, UserSerializer
from account.models import Avatar, User

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination


class AvatarAPIViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all().order_by('-id')
    serializer_class = AvatarSerializer
    pagination_class = PageNumberPagination
