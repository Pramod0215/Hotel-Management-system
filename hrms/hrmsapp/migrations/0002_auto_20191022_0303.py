# Generated by Django 2.2.6 on 2019-10-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='booking_date',
            field=models.DateField(auto_now=True),
        ),
    ]
