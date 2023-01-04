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
    book = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True, "id":"books"}))

    class Meta(BookInfo.Meta):
        fields = BookInfo.Meta.fields + [
            "book",
        ]


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2", "library_no", "first_name", "last_name",]
        help_texts = {
            "username":None,
        }
        labels = {
        }
        widgets = {
            "username": forms.TextInput(attrs={
                "id":"input_46",
                "name":"q46_typeA46",
                "data-type":"input-textbox",
                "class":"form-textbox validate[required]",
                "size":"310",
                "data-component":"textbox",
                "aria-labelledby":"label_46"
            }),
            "first_name":forms.TextInput(attrs={
                "id":"first_4",
                "name":"q4_name[first]",
                "class":"form-textbox validate[required]",
                "autoComplete":"section-input_4 given-name",
                "data-component":"first", 
                "aria-labelledby":"label_4 sublabel_4_first", 
                "required":True,
            }),
            "last_name":forms.TextInput(attrs={
                "id":"last_4",
                "name":"q4_name[last]", 
                "class":"form-textbox validate[required]", 
                "autoComplete":"section-input_4 family-name",  
                "data-component":"last", 
                "aria-labelledby":"label_4 sublabel_4_last", 
                "required":True,
            }),
            "email":forms.EmailInput(attrs={
                "id=":"input_10", 
                "name":"q10_email10",
                "class":"form-textbox validate[required, Email]", 
                "placeholder":"ex: myname@example.com",
                "data-component":"email", 
                "aria-labelledby":"label_10 sublabel_input_10",
                "required":True
            }),
            "password": forms.PasswordInput(attrs={
                "id":"first_50", 
                "name":"q50_name50[first]",
                "class":"form-textbox",  
                "autoComplete":"section-input_50 given-name",  
                "data-component":"first", 
                "aria-labelledby":"label_50 sublabel_50_first", 
                "required":True
            }),
            "password2": forms.PasswordInput(attrs={
                "id":"last_50", 
                "name":"q50_name50[last]",
                "class":"form-textbox", 
                "autoComplete":"section-input_50 family-name",
                "data-component":"last", 
                "aria-labelledby":"label_50 sublabel_50_last",
                "required": False
            }),
            "library_no": forms.TextInput(attrs={"required": False}),
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
        widget=forms.TextInput(attrs={"class":"input100"}),
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={"class":"input100"}),
    )

class Borrow(forms.ModelForm):
    """
    Borrow form
    """
    class Meta:
        model = BorrowBook
        exclude =  ["member",]