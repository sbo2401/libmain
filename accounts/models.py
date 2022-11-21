from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date

# Create your models here.
GENDER = (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("OTHERS", "Prefer not to say"),
)

class Register(models.Model):
    username = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    dob = models.DateField(null=True, blank=False)
    gender = models.CharField(choices=GENDER, default="", max_length=255, null=True)
    pass1 = models.CharField(max_length=255, default="")
    pass2 = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.username





class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Detail(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default="")
   title = models.CharField(max_length=200, default="")
   description = models.CharField(max_length=255, default="")

   def __str__(self):
    return self.title
