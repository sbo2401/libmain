# Generated by Django 4.1.2 on 2022-12-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_alter_user_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password2",
            field=models.CharField(
                default="", max_length=255, null=True, verbose_name="Confirm Password"
            ),
        ),
    ]