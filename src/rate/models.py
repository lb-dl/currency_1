from django.core.cache import cache
from django.db import models

from rate import choices


# Create a model Rate here
class Rate(models.Model):

    source = models.PositiveSmallIntegerField(choices=choices.SOURCE_CHOICES)
    currency = models.PositiveSmallIntegerField(choices=choices.CURRENCY_CHOICES)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        key = self.__class__.cache_key()
        cache.delete(key)

    @classmethod
    def cache_key(cls):
        return 'key'


class ContactUs(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    text = models.TextField()


class Feedback(models.Model):
    raiting = models.CharField(max_length=2)
    text = models.TextField()
