from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_file_extension(value):
        import os
        from django.core.exceptions import ValidationError
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        valid_extensions = [".jpg", ".png", ".jpeg"]
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
    profile_picture = models.ImageField(blank=True, null=True, default="", upload_to="media/images", validators=[validate_file_extension])
    matricno = models.CharField(max_length=9, default="", primary_key=True)
    email = models.EmailField(default="")
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "Users Profile"

    def __str__(self):
        return self.first_name+ " "+self.last_name
