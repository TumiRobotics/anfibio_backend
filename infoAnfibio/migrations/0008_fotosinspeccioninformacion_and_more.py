# Generated by Django 4.1.4 on 2022-12-22 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoAnfibio', '0007_inspeccionmultimediadatos'),
    ]

    operations = [
        migrations.CreateModel(
            name='fotosInspeccionInformacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoInspeccion', models.CharField(default='INSP-0000,FOT-0000', max_length=128)),
                ('rutaInspeccion', models.CharField(default='INSP-0000/', max_length=128)),
                ('rutaFoto', models.CharField(default='', max_length=128)),
                ('codigoFoto', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='inspeccionmultimediadatos',
            name='fechaInspeccion',
            field=models.CharField(default=datetime.datetime(2022, 12, 22, 20, 26, 58, 250581), max_length=128),
        ),
    ]