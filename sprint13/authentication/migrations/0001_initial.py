# Generated by Django 4.1 on 2022-11-09 22:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.BigAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("middle_name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=1001)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "role",
                    models.IntegerField(
                        choices=[(0, "visitor"), (1, "admin")], default=0
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
