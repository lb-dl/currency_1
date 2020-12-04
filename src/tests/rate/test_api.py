# from django.test import TestCase
from account.models import User

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


def test_api_client_auth():

    # creat a user
    email = 'example123421@mail.com'
    user = User.objects.create(username=email, email=email)
    user.set_password(email)
    user.save()

    # make a get request
    client = APIClient()
    response = client.get(reverse('api-rate:rate-list'))

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # make a post request to obtain 'access' and 'refresh' tokens
    response = client.post(
        reverse('token_obtain_pair'),
        data={'password': email, 'email': email},
    )

    assert response.status_code == status.HTTP_200_OK, response.content
    assert "access" in response.json(), response.content
    assert "refresh" in response.json(), response.content

    # set credentials
    token = response.json()['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    # make a get request to get a list of rates
    response = client.get(reverse('api-rate:rate-list'))

    assert response.status_code == status.HTTP_200_OK
