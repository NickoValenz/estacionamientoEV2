# Generated by Django 3.2 on 2024-11-15 02:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEstacionamiento', '0005_auto_20241114_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteest',
            name='rut',
            field=models.CharField(help_text=" (ej.'12345678-9')", max_length=10, validators=[django.core.validators.RegexValidator(message='Rut sin puntos y guion. ', regex='^\\d{7,8}-[\\dkK]$')]),
        ),
        migrations.AlterField(
            model_name='clienteest',
            name='telefono',
            field=models.CharField(help_text=" (ej.'912345678').", max_length=9, validators=[django.core.validators.RegexValidator(message='El telefono debe contener 9 dígitos.', regex='^\\d{9}$')]),
        ),
    ]
