# Generated by Django 4.1.5 on 2023-01-12 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beansapp', '0014_remove_order_product_remove_order_quantity_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beansapp.order'),
        ),
    ]
