# Generated by Django 4.2.7 on 2024-10-25 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Medication",
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
                ("name", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Prescription",
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
                ("amount", models.FloatField()),
                (
                    "measurement",
                    models.CharField(
                        choices=[
                            ("mg", "Milligrams"),
                            ("gm", "Grams"),
                            ("ml", "Milliliters"),
                            ("cp", "Cups"),
                        ],
                        default="mg",
                        max_length=2,
                    ),
                ),
                (
                    "medication",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="meds.medication",
                    ),
                ),
            ],
        ),
    ]