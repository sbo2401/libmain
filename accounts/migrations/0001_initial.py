# Generated by Django 4.1.2 on 2022-11-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Register",
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
                ("username", models.CharField(default="", max_length=255)),
                ("email", models.EmailField(default="", max_length=255)),
                ("dob", models.DateField(default="")),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("OTHERS", "Prefer not to say"),
                        ],
                        default="",
                        max_length=255,
                    ),
                ),
                ("pass1", models.CharField(default="", max_length=255)),
                ("pass2", models.CharField(default="", max_length=255)),
            ],
        ),
    ]
