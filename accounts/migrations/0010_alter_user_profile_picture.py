# Generated by Django 4.1.2 on 2022-12-14 13:00

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_user_password2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="",
                null=True,
                upload_to="media/images",
                validators=[accounts.models.validate_pic_extension],
            ),
        ),
    ]
