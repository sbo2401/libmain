# Generated by Django 4.1.2 on 2023-01-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, default="", max_length=255, unique=True
            ),
        ),
    ]
