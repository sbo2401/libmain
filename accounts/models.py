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

# Create your models here.
class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

class UserProfile(models.Model):
    """
    This is the one for model.py
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="")
    profile_picture = models.FileField(blank=True, null=True, default="", upload_to="media/images", validators=[validate_pic_extension])
    matricno = models.CharField(max_length=9, default="", primary_key=True)
    email = models.EmailField(default="")
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "Users Profile"

    def __str__(self):
        return self.first_name+ " "+self.last_name


class Books(models.Model):
    """
    This is for models.py
    """
    book_title = models.CharField(max_length=255, default="", primary_key=True)
    # book_author = models.CharField(max_length=255, default="")
    # publication_year = models.CharField(max_length=4, default="")
    # isbn = models.CharField(default="", max_length=25)
    book = models.FileField(default="", upload_to="media/books", validators=[validate_book_extension], verbose_name="book Name")

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.book_title