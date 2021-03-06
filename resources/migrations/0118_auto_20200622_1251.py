# Generated by Django 2.2.11 on 2020-06-22 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0117_auto_20200520_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationHomeMunicipalityField',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('name_fi', models.CharField(max_length=100, null=True, unique=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, unique=True, verbose_name='Name')),
                ('name_sv', models.CharField(max_length=100, null=True, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Reservation home municipality field',
                'verbose_name_plural': 'Reservation home municipality fields',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ReservationHomeMunicipalitySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time of creation')),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time of modification')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservationhomemunicipalityset_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('included_municipalities', models.ManyToManyField(related_name='home_municipality_included_set', to='resources.ReservationHomeMunicipalityField', verbose_name='Included municipalities')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservationhomemunicipalityset_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'Reservation home municipality set',
                'verbose_name_plural': 'Reservation home municipality sets',
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='home_municipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.ReservationHomeMunicipalityField', verbose_name='Home municipality'),
        ),
        migrations.AddField(
            model_name='resource',
            name='reservation_home_municipality_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_municipality_included_set', to='resources.ReservationHomeMunicipalitySet', verbose_name='Reservation home municipality set'),
        ),
    ]
