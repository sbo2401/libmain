# Generated by Django 4.1.2 on 2022-11-22 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_detail_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="detail",
            old_name="user",
            new_name="username",
        ),
    ]
