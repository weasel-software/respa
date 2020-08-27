# Generated by Django 2.2.11 on 2020-08-25 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0120_auto_20200724_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcegroup',
            options={'ordering': ('name',), 'permissions': [('group:can_approve_reservation', 'Can approve reservation'), ('group:can_make_reservations', 'Can make reservations'), ('group:can_modify_reservations', 'Can modify reservations'), ('group:can_ignore_opening_hours', 'Can make reservations outside opening hours'), ('group:can_view_reservation_access_code', 'Can view reservation access code'), ('group:can_view_reservation_extra_fields', 'Can view reservation extra fields'), ('group:can_view_reservation_user', 'Can view reservation user'), ('group:can_access_reservation_comments', 'Can access reservation comments'), ('group:can_comment_reservations', 'Can create comments for a reservation'), ('group:can_view_reservation_catering_orders', 'Can view reservation catering orders'), ('group:can_modify_reservation_catering_orders', 'Can modify reservation catering orders'), ('group:can_view_reservation_product_orders', 'Can view reservation product orders'), ('group:can_modify_paid_reservations', 'Can modify paid reservations'), ('group:can_bypass_payment', 'Can bypass payment for paid reservations'), ('group:can_create_staff_event', 'Can create a reservation that is a staff event'), ('group:can_create_special_type_reservation', 'Can create reservations of a non-normal type'), ('group:can_bypass_manual_confirmation', 'Can bypass manual confirmation requirement for resources'), ('group:can_create_reservations_for_other_users', 'Can create reservations for other registered users'), ('group:can_create_overlapping_reservations', 'Can create overlapping reservations'), ('group:can_ignore_max_reservations_per_user', 'Can ignore resources max reservations per user rule'), ('group:can_ignore_max_period', 'Can ignore resources max period rule'), ('group:can_modify_opening_hours', 'Can modify opening hours')], 'verbose_name': 'Resource group', 'verbose_name_plural': 'Resource groups'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ('name',), 'permissions': [('unit:can_approve_reservation', 'Can approve reservation'), ('unit:can_make_reservations', 'Can make reservations'), ('unit:can_modify_reservations', 'Can modify reservations'), ('unit:can_ignore_opening_hours', 'Can make reservations outside opening hours'), ('unit:can_view_reservation_access_code', 'Can view reservation access code'), ('unit:can_view_reservation_extra_fields', 'Can view reservation extra fields'), ('unit:can_view_reservation_user', 'Can view reservation user'), ('unit:can_access_reservation_comments', 'Can access reservation comments'), ('unit:can_comment_reservations', 'Can create comments for a reservation'), ('unit:can_view_reservation_catering_orders', 'Can view reservation catering orders'), ('unit:can_modify_reservation_catering_orders', 'Can modify reservation catering orders'), ('unit:can_view_reservation_product_orders', 'Can view reservation product orders'), ('unit:can_modify_paid_reservations', 'Can modify paid reservations'), ('unit:can_bypass_payment', 'Can bypass payment for paid reservations'), ('unit:can_create_staff_event', 'Can create a reservation that is a staff event'), ('unit:can_create_special_type_reservation', 'Can create reservations of a non-normal type'), ('unit:can_bypass_manual_confirmation', 'Can bypass manual confirmation requirement for resources'), ('unit:can_create_reservations_for_other_users', 'Can create reservations for other registered users'), ('unit:can_create_overlapping_reservations', 'Can create overlapping reservations'), ('unit:can_ignore_max_reservations_per_user', 'Can ignore resources max reservations per user rule'), ('unit:can_ignore_max_period', 'Can ignore resources max period rule'), ('unit:can_modify_opening_hours', 'Can modify opening hours')], 'verbose_name': 'unit', 'verbose_name_plural': 'units'},
        ),
    ]
