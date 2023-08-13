# Generated by Django 4.2.1 on 2023-08-12 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("empresas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Moneda",
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
                ("descripcion", models.CharField(max_length=50)),
                ("sigla", models.CharField(verbose_name=10)),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="empresas.empresa",
                    ),
                ),
            ],
            options={
                "db_table": "monedas",
            },
        ),
    ]