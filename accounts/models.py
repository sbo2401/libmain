from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_pic_extension(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".jpg", ".png", ".jpeg"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")


def validate_book_extension(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".pdf", ".epub"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")


# Create your models here


class User(AbstractUser):
    profile_picture = models.ImageField(
        blank=True,
        null=True,
        default="",
        upload_to="images",
        validators=[validate_pic_extension],
    )
    password2 = models.CharField(default="", max_length=128, verbose_name="Confirm Password", null=True, blank=True)
    def __str__(self):
        return self.username


# class UserProfile(models.Model):
#     """
#     This is the one for model.py
#     """

#     username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="")
#     matricno = models.CharField(max_length=9, default="", primary_key=True)
#     email = models.EmailField(default="")
#     first_name = models.CharField(max_length=200, default="")
#     last_name = models.CharField(max_length=255, default="")

#     class Meta:
#         verbose_name_plural = "Users Profile"

#     def __str__(self):
#         return self.first_name + " " + self.last_name


class Catalog(models.Model):
    catalog_name = models.CharField(default="", max_length=255)


class Collection(models.Model):
    collection_name = models.CharField(default="", max_length=255)


class Genre(models.Model):
    genres = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.genres


class Books(models.Model):
    """
    This is for models.py
    """

    book_title = models.CharField(max_length=255, default="", primary_key=True)
    book = models.FileField(
        default="",
        upload_to="books",
        validators=[validate_book_extension],
        verbose_name="books",
    )
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default="")

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.book_title
