# Generated by Django 4.1.5 on 2023-01-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beansapp', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsinorder',
            name='quantity',
            field=models.CharField(max_length=10),
        ),
    ]
