# Generated by Django 4.1.2 on 2022-12-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_remove_books_book_author_remove_books_isbn_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="books",
            name="id",
        ),
        migrations.AlterField(
            model_name="books",
            name="book_title",
            field=models.CharField(
                default="", max_length=255, primary_key=True, serialize=False
            ),
        ),
    ]
