# Generated by Django 4.1.4 on 2022-12-22 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoAnfibio', '0009_alter_inspeccionmultimediadatos_fechainspeccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspeccionmultimediadatos',
            name='codigoInspeccion',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='inspeccionmultimediadatos',
            name='fechaInspeccion',
            field=models.CharField(default=datetime.datetime(2022, 12, 22, 21, 16, 33, 234595), max_length=128),
        ),
    ]