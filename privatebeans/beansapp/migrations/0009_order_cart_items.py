# Generated by Django 4.1.5 on 2023-01-10 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beansapp', '0008_alter_productsinorder_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_items',
            field=models.ManyToManyField(through='beansapp.ProductsInOrder', to='beansapp.product'),
        ),
    ]
