# Generated by Django 4.1.5 on 2023-01-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beansapp', '0007_remove_order_cart_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsinorder',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
