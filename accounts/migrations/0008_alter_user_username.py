# Generated by Django 4.1.2 on 2023-01-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_borrowbook_library_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(default="", max_length=9, unique=True),
        ),
    ]
