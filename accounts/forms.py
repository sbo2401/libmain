from django import forms
from django.contrib.auth.forms import *
from accounts.models import *
from django.contrib.auth import get_user_model
User =get_user_model()

class Details(forms.ModelForm):
   class Meta:
    model = Detail
    exclude = ["username"]
    widgets={
        "matricno": forms.TextInput(attrs={"readonly":"readonly"})
    }


class Signup(forms.Form):
    username = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Matric Number"}),
    )

    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={"placeholder": "Enter Your E-mail Address"}),
    )

    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Your Password", "id": "password"}
        ),
    )

    password2 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Your Password", "id": "password2"}
        ),
    )
    
    def clean(self):
        super(Signup, self).clean()
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")

        if password != password2:
            self.errors[""] = self.error_class(["The two password fields must match"])

        for instance in User.objects.all():
            if instance.username == str(username):
                self.errors[""] = self.error_class(["User already exist"])
            elif instance.email == email:
                self.errors[""] = self.error_class(["E-mail already in use"])
            else:
                pass

        return self.cleaned_data

class Signin(forms.Form):
    username = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Userame"}),
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Your Password", "id": "password"}
        ),
    )

    
# class Register(forms.ModelForm):
#     class Meta:
#         model = Register 
#         exclude = ("dob", "gender",)
#         widgets={
#             "pass1":forms.PasswordInput(attrs={
#                 "placeholder":"Enter Your Preffered Password"
#             }),
#             "pass2":forms.PasswordInput(attrs={
#                 "placeholder":"Confirm Your Password"
#             }),
#             "dob": forms.DateInput(attrs={
#                 "type":"date",
#             }),
#             "gender": forms.RadioSelect(attrs={
#                 "type":"radio"
#             }),
#             "username":forms.TextInput(attrs={
#                 "placeholder":"Enter Your Username",
#             }),
#             "email":forms.EmailInput(attrs={
#                 "placeholder":"Enter your E-mail"
#             })
#         }
#     def clean(self):
#         super(Register, self).clean()
#         pass1 = self.cleaned_data.get("pass1")
#         pass2 = self.cleaned_data.get("pass2")
#         username = self.cleaned_data.get("username")
#         email = self.cleaned_data.get("email")

#         if pass1 != pass2:
#             self.errors[""] = self.error_class(["The two password fields must match"])

class Signin(forms.Form):
    username = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Userame"}),
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Your Password", "id": "password"}
        ),
    )

