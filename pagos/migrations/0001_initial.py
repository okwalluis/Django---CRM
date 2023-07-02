# Generated by Django 4.2.1 on 2023-06-25 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "prestamos",
            "0010_alter_prestamo_created_by_alter_prestamo_modified_at_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Pago",
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
                ("fecha_pago", models.DateField()),
                ("monto_pago", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "cuota",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="prestamos.cuotaprestamo",
                    ),
                ),
            ],
            options={
                "db_table": "pagos",
            },
        ),
    ]
