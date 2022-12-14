from django import forms
from django.contrib.auth.forms import *
from accounts.models import *
from django.contrib.auth import get_user_model

User = get_user_model()


# class Details(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         exclude = ["username"]
#         widgets = {"matricno": forms.TextInput(attrs={"readonly": True})}

#     def clean(self):
#         super(Details, self).clean()
#         email = self.cleaned_data.get("email")
#         profile_picture = self.cleaned_data.get("profile_picture", False)
#         if profile_picture:
#             if profile_picture.size > 4000000:
#                 self.errors[""] = self.error_class(["Picture larger than 4MB"])
#         return self.cleaned_data


class BookInfo(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            "genres",
        ]
        widgets = {"genres": forms.TextInput(attrs={"list": "genres"})}


class BookFile(BookInfo):
    book = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta(BookInfo.Meta):
        fields = BookInfo.Meta.fields + [
            "book",
        ]


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2", "profile_picture"]
        help_texts = {
            "username":None
        }
        widgets = {
            "username": forms.TextInput(),
            "password": forms.PasswordInput(),
            "password2": forms.PasswordInput(attrs={"required": True}),
        }


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
