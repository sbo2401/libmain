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


#         return self.cleaned_data


class BookInfo(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            "genres",
        ]
        widgets = {"genres": forms.TextInput(attrs={"list": "genres"})}


class BookFile(BookInfo):
    book = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True, "id": "books"})
    )

    class Meta(BookInfo.Meta):
        fields = BookInfo.Meta.fields + [
            "book",
        ]


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
            "library_no",
            "first_name",
            "last_name",
        ]
        help_texts = {
            "username": None,
        }
        labels = {}
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "id": "input_64",
                    "name": "q64_typeA",
                    "data-type": "input-textbox",
                    "class": "form-textbox validate[required]",
                    "data-defaultvalue": "",
                    "size": "20",
                    "value": "",
                    "placeholder": "180591001",
                    "data-component": "textbox",
                    "aria-labelledby": "label_64",
                    "required": "",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "id": "first_65",
                    "name": "q65_name[first]",
                    "class": "form-textbox validate[required]",
                    "data-defaultvalue": "",
                    "autoComplete": "section-input_65 given-name",
                    "size=": "10",
                    "value": "",
                    "data-component": "first",
                    "aria-labelledby": "label_65 sublabel_65_first",
                    "required": "",
                    "placeholder": "Chinedu",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "id": "first_66",
                    "name": "q66_name[first]",
                    "class": "form-textbox validate[required]",
                    "data-defaultvalue": "",
                    "autoComplete": "section-input_66 given-name",
                    "size": "10",
                    "value": "",
                    "data-component": "first",
                    "aria-labelledby": "label_66 sublabel_66_first",
                    "required": "",
                    "placeholder": "Oladapo Dikko",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "id": "input_67",
                    "name": "q67_email",
                    "class": "form-textbox validate[required, Email]",
                    "data-defaultvalue": "",
                    "size": "30",
                    "value": "",
                    "data-component": "email",
                    "aria-labelledby": "label_67",
                    "required": "",
                    "placeholder": "abc@example.com",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "id": "first_66",
                    "name": "q66_name66[first]",
                    "class": "form-textbox validate[required]",
                    "data-defaultvalue": "",
                    "autoComplete": "section-input_66 given-name",
                    "size": "10",
                    "value": "",
                    "data-component": "first",
                    "aria-labelledby": "label_66 sublabel_66_first",
                    "required": "",
                    "placeholder": "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "id": "first_66",
                    "name": "q66_name66[first]",
                    "class": "form-textbox validate[required]",
                    "data-defaultvalue": "",
                    "autoComplete": "section-input_66 given-name",
                    "size": "10",
                    "value": "",
                    "data-component": "first",
                    "aria-labelledby": "label_66 sublabel_66_first",
                    "required": "",
                    "placeholder": "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022",
                }
            ),
        }

    def clean(self):
        super(Signup, self).clean()
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        avatar = self.cleaned_data.get("avatar", False)

        if password != password2:
            self.errors[""] = self.error_class(["The two password fields must match"])
        elif avatar:
            if avatar.size > 4000000:
                self.errors[""] = self.error_class(["Picture larger than 4MB"])
        for instance in User.objects.all():
            # if instance.username == str(username):
            #     self.errors[""] = self.error_class(["User already exist"])
            if instance.email == email:
                self.errors[""] = self.error_class(["E-mail already in use"])
            else:
                pass

        return self.cleaned_data


class Signin(forms.Form):
    username = forms.CharField(
        max_length=9,
        widget=forms.TextInput(
            attrs={
                "id": "input_64",
                "name": "q64_typeA",
                "data-type": "input-textbox",
                "class": "form-textbox validate[required]",
                "data-defaultvalue": "",
                "size": "20",
                "value": "",
                "placeholder": "180591001",
                "data-component": "textbox",
                "aria-labelledby": "label_64",
                "required": "",
            }
        ),
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "id": "first_66",
                "name": "q66_name66[first]",
                "class": "form-textbox validate[required]",
                "data-defaultvalue": "",
                "autoComplete": "section-input_66 given-name",
                "size": "10",
                "value": "",
                "data-component": "first",
                "aria-labelledby": "label_66 sublabel_66_first",
                "required": "",
                "placeholder": "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022",
            }
        ),
    )


class Profile(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            
        ]

class Borrow(forms.ModelForm):
    """
    Borrow form
    """

    class Meta:
        model = BorrowBook
        exclude = [
            "member",
        ]
class Idkk(forms.ModelForm):
    class Meta:
        model = Idk
        fields = "__all__"