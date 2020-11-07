from django.urls import reverse


def test_feedback_get_form(client):
    url = reverse('rate:feedback-create')
    response = client.get(url)
    assert response.status_code == 200
