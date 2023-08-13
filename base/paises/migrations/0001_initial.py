# Generated by Django 4.2.1 on 2023-08-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pais",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=80)),
                ("sigla", models.CharField(max_length=5)),
                ("activo", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "paises",
            },
        ),
    ]