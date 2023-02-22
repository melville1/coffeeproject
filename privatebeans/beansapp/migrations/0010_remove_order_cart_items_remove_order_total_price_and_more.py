# Generated by Django 4.1.5 on 2023-01-11 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beansapp', '0009_order_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='order_quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beansapp.product'),
        ),
        migrations.DeleteModel(
            name='ProductsInOrder',
        ),
    ]