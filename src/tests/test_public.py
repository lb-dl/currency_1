from django.urls import reverse

from rate.models import ContactUs


def test_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200


def test_contact_us_get_form(client):
    url = reverse('rate:contact-us-create')
    response = client.get(url)
    assert response.status_code == 200


def test_contact_us_post_empty_data(client):
    url = reverse('rate:contact-us-create')
    response = client.post(url, data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['This field is required.'],
        'subject': ['This field is required.'],
        'text': ['This field is required.']
    }


def test_contact_us_post_wrong_email(client):
    url = reverse('rate:contact-us-create')
    contact_us_initial_count = ContactUs.objects.count()
    data = {
        'email': 'This-is-wrong-email',
        'subject': 'Subject',
        'text': 'Message'
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Enter a valid email address.']
    }
    assert ContactUs.objects.count() == contact_us_initial_count


def test_contact_us_post_correct_data(client, fake):
    url = reverse('rate:contact-us-create')
    contact_us_initial_count = ContactUs.objects.count()
    data = {
        'email': 'This-is-correct-email@gmail.com',
        'subject': fake.word(),
        'text': fake.word(),
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert ContactUs.objects.count() == contact_us_initial_count + 1


def test_fixt(user_fix):
    pass
