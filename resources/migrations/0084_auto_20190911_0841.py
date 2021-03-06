# Generated by Django 2.1.12 on 2019-09-11 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0083_reservation_preferred_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='reservation_extra_questions',
            new_name='reservation_additional_information',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='reservation_extra_questions_en',
            new_name='reservation_additional_information_en',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='reservation_extra_questions_fi',
            new_name='reservation_additional_information_fi',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='reservation_extra_questions_sv',
            new_name='reservation_additional_information_sv',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_extra_questions_en',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_extra_questions_fi',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_extra_questions_sv',
        ),
    ]
