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
    username = models.CharField(max_length=9, default="", verbose_name="User Id", unique=True) 
    avatar = models.ImageField(
        blank=True,
        null=True,
        default="avatar.svg",
        upload_to="images",
        validators=[validate_pic_extension],
    )
    password2 = models.CharField(default="", max_length=128, verbose_name="Confirm Password", null=True, blank=True)

    def __str__(self):
        return self.username


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
    title = models.CharField(max_length=500, default="")
    author = models.CharField(max_length=500, default="")
    publication = models.CharField(max_length=500, default="")
    edition = models.IntegerField(default="")
    is_available = models.BooleanField()
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
        return self.title
class BorrowBook(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, default="")


class BorrowedBook(models.Model):
    member = models.ForeignKey(User, on_delete=models.SET_NULL, default="", null=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True, default="")
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField()
    is_returned = models.BooleanField()

