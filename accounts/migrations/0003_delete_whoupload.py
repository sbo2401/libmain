# Generated by Django 4.1.2 on 2023-01-01 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_whoupload"),
    ]

    operations = [
        migrations.DeleteModel(
            name="WhoUpload",
        ),
    ]