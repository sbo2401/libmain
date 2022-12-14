from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_pic_extension(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".jpg", ".png", ".jpeg", ".hiec"]
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

DESIGNATION = (
    ("Staff", "Staff"),
    ("Student", "Student"),
)

LIBUSER = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class User(AbstractUser):
    username = models.CharField(max_length=9, default="", unique=True)
    avatar = models.ImageField(
        blank=True,
        null=True,
        default="avatar.svg",
        upload_to="images",
        validators=[validate_pic_extension],
    )
    password2 = models.CharField(
        default="",
        max_length=128,
        verbose_name="Confirm Password",
        null=True,
        blank=True,
    )
    email = models.EmailField(default="", max_length=255, unique=True)
    designation = models.CharField(
        default="", choices=DESIGNATION, max_length=255, null=True, blank=True
    )
    staff_id = models.CharField(
        default="", max_length=255, null=True, blank=True, verbose_name="Staff Id"
    )
    matric_no = models.CharField(
        default="", max_length=255, null=True, blank=True, verbose_name="Matric Number"
    )
    lib_user = models.CharField(
        default="",
        max_length=255,
        choices=LIBUSER,
        null=True,
        blank=True,
        verbose_name="Library User",
    )
    library_id = models.CharField(
        default="",
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Library Card Id",
    )

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
    library_no = models.CharField(default="", max_length=15, blank=True)

    def __str__(self):
        return (str(self.member)) + " " + "applied to borrow " + (str(self.book))


class BorrowedBook(models.Model):
    member = models.ForeignKey(User, on_delete=models.SET_NULL, default="", null=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True, default="")
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField()
    is_returned = models.BooleanField()


class Idk(models.Model):
    name = models.CharField(default="", max_length=128)


class Student(models.Model):
    # name = models.CharField(max_length=255, null=True, blank=True)
    # codePerm = models.CharField(max_length=200, null=True, blank=True)
    files = models.FileField(upload_to="files", blank=True, null=True)
