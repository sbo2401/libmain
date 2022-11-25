from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth
from django.contrib.auth import logout, login, authenticate

User =get_user_model()
# Create your views here.

def success(request):
    return render(request, "success.html", {})

def edit(request, pk):
    detail = Detail.objects.get(matricno=pk)
    form = Details(instance=detail)

    if request.method == "POST":
        form = Details(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect(success)
    return render(request, "details.html", {"form":form})

def details(request):
    form = Details()
    if request.method == "POST":
        form = Details(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = Details()
    return render(request, "details.html", {"form":form})


