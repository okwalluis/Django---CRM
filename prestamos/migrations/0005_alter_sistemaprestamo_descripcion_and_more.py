# Generated by Django 4.2.1 on 2023-06-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prestamos", "0004_alter_frecuenciapagoprestamo_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sistemaprestamo",
            name="descripcion",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="tipoprestamo",
            name="descripcion",
            field=models.CharField(max_length=50),
        ),
    ]
