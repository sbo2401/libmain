import email
from email.policy import default
from django.db import models

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


class Detail(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    middle_name = models.CharField(max_length=255, default="")
    about = models.TextField(max_length=255, default="")

    def __str__(self):
        return self.first_name+" " +self.middle_name+" " +self.last_name