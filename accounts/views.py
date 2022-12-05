from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

User =get_user_model()
# Create your views here.

def index(request):
    return render(request, "index.html", {})

def success(request,pk):
    return render(request, "success.html", {"pk":pk})

@login_required(login_url="signin")
def details(request):
    # user = User.objects.get(username=username)
    form = Details()
    if request.method == "POST":
        form = Details(request.POST, request.FILES)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.username = request.user
            detail.save()
            return redirect(success, pk=detail.pk)
    else:
        form = Details(initial={"matricno":request.user.username})
    return render(request, "details.html", {"form":form})

def updatedetails(request, pk):
    detail = UserProfile.objects.get(matricno=pk)
    form = Details(instance=detail)
    if request.method == "POST":
        form = Details(request.POST, request.FILES, instance=detail,)
        if form.is_valid():
            form.save()
            return redirect(success, pk=detail.pk)
    return render(request, "update.html", {"form":form})

def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            password2 = request.POST["password2"]

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            user.save()
            login(request, user)
            messages.success(request, "Account Created successfully for " + username)
            return redirect(details)
    else:
        form = Signup()
    return render(request, "accounts/register.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return redirect(details)
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
                    messages.error(request, "You have entered an incorrect password")
                    return redirect(signin)
                else:
                    login(request, get_user[0])
                    return redirect(index)
            else:
                messages.error(request, "User does not exist")
                return redirect(signin)
    else:
        form = Signin()
        return render(request, "accounts/login.html", {"form": form})

def signout(request):
    logout(request)
    return redirect(index)