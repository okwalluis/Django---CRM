# Generated by Django 4.2.1 on 2023-06-25 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("prestamos", "0008_rename_fecha_inicio_prestamo_fecha_primer_vencimiento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prestamo",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="prestamo",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="prestamo",
            name="nro_prestamo",
            field=models.IntegerField(null=True),
        ),
    ]
