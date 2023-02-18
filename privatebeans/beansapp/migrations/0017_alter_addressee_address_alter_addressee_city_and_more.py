# Generated by Django 4.1.5 on 2023-02-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beansapp', '0016_remove_addressee_name_addressee_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressee',
            name='address',
            field=models.EmailField(max_length=15),
        ),
        migrations.AlterField(
            model_name='addressee',
            name='city',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='addressee',
            name='first_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='addressee',
            name='last_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='addressee',
            name='state',
            field=models.CharField(max_length=15),
        ),
    ]
