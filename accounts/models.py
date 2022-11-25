from django.db import models
from django.contrib.auth.models import AbstractUser


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
    """
    This is the one for model.py
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default="")
    matricno = models.CharField(max_length=9, default="", primary_key=True)
    email = models.EmailField(default="")
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = "Detail"

    def __str__(self):
        return self.first_name+ " "+self.last_name
