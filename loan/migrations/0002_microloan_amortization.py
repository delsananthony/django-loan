# Generated by Django 4.2.3 on 2023-07-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loan", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="microloan",
            name="amortization",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                max_digits=10,
                verbose_name="Amortization",
            ),
        ),
    ]
