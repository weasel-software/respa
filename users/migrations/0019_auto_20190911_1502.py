# Generated by Django 2.1.12 on 2019-09-11 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20190911_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Birthday'),
        ),
    ]
