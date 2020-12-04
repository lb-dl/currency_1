import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField('email address', blank=False, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = str(uuid.uuid4())
        super().save(*args, **kwargs)


def user_avatar_upload(instance, filename):
    return f'{instance.user_id}/{filename}'


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to=user_avatar_upload)

    def delete(self, *args, **kwargs):
        self.file_path.delete()
        super().delete(*args, **kwargs)
