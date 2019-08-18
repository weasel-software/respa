# Generated by Django 2.1.7 on 2019-07-10 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0017_change_product_price_taxful'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('product_id',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(db_index=True, editable=False, max_length=100, verbose_name='internal product ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='resources',
            field=models.ManyToManyField(blank=True, related_name='products', to='resources.Resource', verbose_name='resources'),
        ),
    ]