# Generated by Django 3.2 on 2024-10-25 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appEstacionamiento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clienteest',
            name='telefono',
        ),
    ]
