from django.urls import reverse


def test_selectors(client):
    response = client.get(reverse('rate:list-latest'))
    assert response.status_code == 200
