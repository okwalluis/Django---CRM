# Generated by Django 4.2.1 on 2023-08-12 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("empresas", "0001_initial"),
        ("productos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lote",
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
                ("nro_lote", models.CharField(default="0000", max_length=30)),
                ("fecha_elaboracion", models.DateField()),
                ("fecha_vencimiento", models.DateField()),
                ("descripcion", models.CharField(max_length=50, unique=True)),
                ("activo", models.BooleanField(default=True)),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="empresas.empresa",
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="productos.producto",
                    ),
                ),
            ],
            options={
                "db_table": "lotes",
            },
        ),
    ]