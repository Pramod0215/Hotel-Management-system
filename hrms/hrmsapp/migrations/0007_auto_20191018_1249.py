# Generated by Django 2.2.6 on 2019-10-18 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0006_auto_20191018_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsapp.Guest'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_avilable', models.BooleanField(default=True)),
                ('cancel', models.BooleanField(default=False)),
                ('hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsapp.Hotel')),
                ('room1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsapp.Room')),
            ],
        ),
    ]
