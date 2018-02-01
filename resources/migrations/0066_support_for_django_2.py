# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-02 19:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0065_add_manager_email_field_to_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='slug',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipment_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipment_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='equipmentalias',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipmentalias_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='equipmentalias',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipmentalias_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='equipmentcategory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipmentcategory_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='equipmentcategory',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipmentcategory_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='purpose',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purpose_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='purpose',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purpose_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='purpose',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='resources.Purpose', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_reservations', to=settings.AUTH_USER_MODEL, verbose_name='Approver'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservation_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservation_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservations', to='resources.Resource', verbose_name='Resource'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='reservationmetadataset',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservationmetadataset_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='reservationmetadataset',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservationmetadataset_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resource_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='generic_terms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.TermsOfUse', verbose_name='Generic terms'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resource_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='reservation_metadata_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.ReservationMetadataSet'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resources.ResourceType', verbose_name='Resource type'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='resources', to='resources.Unit', verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='resourceequipment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resourceequipment_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='resourceequipment',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resourceequipment_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='resourcegroup',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resourcegroup_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='resourcegroup',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resourcegroup_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='resourceimage',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resourceimage_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='resourceimage',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resourceimage_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='resourcetype',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resourcetype_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='resourcetype',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resourcetype_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='termsofuse',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='termsofuse_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='termsofuse',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='termsofuse_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unit_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unit_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='municipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='munigeo.Municipality', verbose_name='Municipality'),
        ),
    ]