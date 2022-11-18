from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth
from django.contrib.auth import logout, login, authenticate

# Create your views here.
def details(request):
    if request.method =="POST":
        form = Details(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.first_name = detail.first_name.lower()
            detail.middle_name = detail.middle_name.lower()
            detail.last_name = detail.last_name.lower()
            detail.about = detail.about.title()
            detail.save()
            return redirect("admin:index")
    else:
        form = Details()
    return render(request, "details.html", {"form":form})