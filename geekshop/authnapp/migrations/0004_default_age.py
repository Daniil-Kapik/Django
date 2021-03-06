# Generated by Django 3.2 on 2022-04-17 10:40

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0003_alter_shopuser_activation_key_expires"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 4, 19, 10, 40, 1, 25681, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
        migrations.AlterField(
            model_name="shopuser",
            name="age",
            field=models.PositiveIntegerField(default=18, verbose_name="возраст"),
        ),
    ]
