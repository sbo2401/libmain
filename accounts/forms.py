from django import forms
from accounts.models import *

class Details(forms.ModelForm):
   class Meta:
    model = Detail
    fields = "__all__"

class Register(forms.ModelForm):
    class Meta:
        model = Register 
        exclude = ("dob", "gender",)
        widgets={
            "pass1":forms.PasswordInput(attrs={
                "placeholder":"Enter Your Preffered Password"
            }),
            "pass2":forms.PasswordInput(attrs={
                "placeholder":"Confirm Your Password"
            }),
            "dob": forms.DateInput(attrs={
                "type":"date",
            }),
            "gender": forms.RadioSelect(attrs={
                "type":"radio"
            }),
            "username":forms.TextInput(attrs={
                "placeholder":"Enter Your Username",
            }),
            "email":forms.EmailInput(attrs={
                "placeholder":"Enter your E-mail"
            })
        }
    def clean(self):
        super(Register, self).clean()
        pass1 = self.cleaned_data.get("pass1")
        pass2 = self.cleaned_data.get("pass2")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")

        if pass1 != pass2:
            self.errors[""] = self.error_class(["The two password fields must match"])

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