# Generated by Django 3.2 on 2022-05-01 18:43

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0008_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 18, 43, 36, 335031, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
