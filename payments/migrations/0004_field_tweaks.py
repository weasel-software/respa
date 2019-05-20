# Generated by Django 2.1.7 on 2019-05-11 19:45

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_product_i18n'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='code',
            new_name='sku',
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=255, verbose_name='SKU'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pretax_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=14, validators=[django.core.validators.MinValueValidator(0)], verbose_name='pretax price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax_percentage',
            field=models.DecimalField(choices=[(Decimal('0.00'), Decimal('0.00')), (Decimal('10.00'), Decimal('10.00')), (Decimal('14.00'), Decimal('14.00')), (Decimal('24.00'), Decimal('24.00'))], decimal_places=2, default=Decimal('24.00'), max_digits=5, verbose_name='tax percentage'),
        ),
    ]
