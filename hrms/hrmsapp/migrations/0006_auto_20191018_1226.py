# Generated by Django 2.2.6 on 2019-10-18 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0005_auto_20191018_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='manager_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manager',
            name='manager_phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsapp.Guest'),
        ),
    ]
