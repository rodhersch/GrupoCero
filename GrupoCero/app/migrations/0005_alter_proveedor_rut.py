# Generated by Django 3.2.5 on 2021-07-07 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_proveedor_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='rut',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut proveedor'),
        ),
    ]
