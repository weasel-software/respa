# Generated by Django 2.2.10 on 2020-03-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0088_disallow_overlapping_reservations_and_accessibility_changes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='max_price_per_hour',
            new_name='max_price',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='min_price_per_hour',
            new_name='min_price',
        ),
        migrations.AddField(
            model_name='resource',
            name='price_type',
            field=models.CharField(choices=[('hourly', 'Hourly'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('fixed', 'Fixed')], default='hourly', max_length=32, verbose_name='price type'),
        ),
    ]
