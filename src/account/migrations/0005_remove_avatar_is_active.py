# Generated by Django 2.2.16 on 2020-12-07 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_avatar_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='is_active',
        ),
    ]