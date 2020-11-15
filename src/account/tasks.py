from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


@shared_task
def send_sign_up_email(user_id: int):
    from account.models import User
    user = User.objects.get(id=user_id)
    url = settings.DOMAIN + reverse('account:activate', args=(user.username, ))
    body = f'''
        URL: {url}
    '''
    send_mail(
        'Sign up',
        body,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
