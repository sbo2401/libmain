# Generated by Django 4.1.2 on 2023-01-01 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_delete_whoupload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowedbook",
            name="book",
            field=models.ForeignKey(
                default="",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.books",
            ),
        ),
        migrations.AlterField(
            model_name="borrowedbook",
            name="member",
            field=models.ForeignKey(
                default="",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="BorrowBook",
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
                (
                    "book",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.books",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
