# Generated by Django 4.1.5 on 2023-02-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beansapp', '0018_alter_addressee_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressee',
            name='password',
            field=models.CharField(max_length=15, null=True),
        ),
    ]