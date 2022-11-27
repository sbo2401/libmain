from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Detail(models.Model):
    """
    This is the one for model.py
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="")
    matricno = models.CharField(max_length=9, default="")
    email = models.EmailField(default="")
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "Detail"

    def __str__(self):
        return self.first_name+ " "+self.last_name
