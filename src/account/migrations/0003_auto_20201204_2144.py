# Generated by Django 2.2.16 on 2020-12-04 21:44

import account.models

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='file_path',
            field=models.FileField(upload_to=account.models.user_avatar_upload),
        ),
    ]
