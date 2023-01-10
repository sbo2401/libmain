from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.db import IntegrityError

User = get_user_model()
# Create your views here.


def index(request):
    return render(request, "index.html", {})


def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password"]
            password2 = request.POST["password2"]

            if "@yahoo.com" or "@ymail.com" in email:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                    email=email,
                )
                user.save()
                login(request, user)
                messages.success(
                    request, "Account Created successfully for " + username
                )
                return redirect(index)
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                    email=email.lower(),
                )
                user.save()
                login(request, user)
                messages.success(
                    request, "Account Created successfully for " + username
                )
                return redirect(index)
    else:
        form = Signup()
    return render(request, "accounts/register.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == "POST":
        form = Signin(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = User.objects.filter(username=username).exists()
            if user:
                get_user = User.objects.filter(username=username)
                check_pass = check_password(password, get_user[0].password)
                if not check_pass:
                    messages.error(request, "incorrect password")
                    return redirect(signin)
                else:
                    login(request, get_user[0])
                    return redirect(index)
            else:
                messages.error(request, "Invalid User")
                return redirect(signin)
    else:
        form = Signin()
        return render(request, "accounts/login.html", {"form": form})


def signout(request):
    logout(request)
    return redirect(index)


# @login_required(login_url="signin")
# def details(request):
#     if request.user.is_authenticated and request.user.is_superuser:
#         return redirect(index)
#     form = Details()
#     if request.method == "POST":
#         form = Details(request.POST, request.FILES)
#         if form.is_valid():
#             detail = form.save(commit=False)
#             detail.username = request.user
#             detail.save()
#             return redirect(success, pk=detail.pk)
#     else:
#         form = Details(initial={"matricno": request.user.username})
#     return render(request, "details.html", {"form": form})


# def success(request, pk):
#     if request.user.is_authenticated and request.user.is_superuser:
#         return redirect(index)
#     else:
#     return render(request, "success.html", {"pk": pk})


# def updatedetails(request, pk):
#     if request.user.is_authenticated and request.user.is_superuser:
#         return redirect(index)
#     detail = UserProfile.objects.get(matricno=pk)
#     form = Details(instance=detail)
#     if request.method == "POST":
#         form = Details(
#             request.POST,
#             request.FILES,
#             instance=detail,
#         )
#         if form.is_valid():
#             form.save()
#             return redirect(success, pk=detail.pk)
#     return render(request, "update.html", {"form": form})


def books(request):
    genres_names = Genre.objects.all()
    if request.method == "POST":
        form = BookFile(request.POST, request.FILES)
        files = request.FILES.getlist("book")
        genres_name = request.POST.get("genres")
        try:
            if form.is_valid():
                new_old_genre, created = Genre.objects.get_or_create(
                    genres=genres_name.lower()
                )
                genre = Genre.objects.filter(genres=genres_name)
                if files:
                    for f in files:
                        names = str(f)
                        name = names.strip(".pdf")
                        Books.objects.create(
                            genre=new_old_genre, book_title=name, book=f
                        )
                return redirect(index)
        except IntegrityError:
            messages.error(request, "value exist in database")
            return redirect(books)
    else:
        form = BookFile()
    return render(request, "books.html", {"form": form, "genres_names": genres_names})


def test(request):
    data = Books.objects.filter(genre__genres="project")
    return render(request, "test.html", {"data": data})


def test1(request):
    return render(request, "test1.html", {})


def borrow(request):
    if request.method == "POST":
        form = Borrow(request.POST)
        if form.is_valid():
            borrower = form.save(commit=False)
            borrower.member = request.user
            borrower.save()
    else:
        form = Borrow(initial={"library_no": request.user.library_no})
    return render(request, "borrow.html", {"form": form})


def profile(request, pk):
    profile = User.objects.get(id=pk)
    form = Profile(instance=profile)
    return render(request, "accounts/profile.html", {"form": form})


def idk(request):
    if request.method == "POST":
        name = request.POST["name"]
        ab = Idk.objects.create(name=name)
        ab.save()

        # return redirect(index)

    return render(request, "success.html")


def upload(request):
    if request.method == "POST":
        form = FileUpload(request.POST, request.FILES)
        file = request.FILES.getlist("files")
        if form.is_valid():
            if file:
                for f in file:
                    Student.objects.create(files=f)
    else:
        form = FileUpload()
    return render(request, "file.html", {"form": form})
