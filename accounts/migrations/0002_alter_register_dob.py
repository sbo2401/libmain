# Generated by Django 4.1.2 on 2022-11-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="register",
            name="dob",
            field=models.DateField(),
        ),
    ]