from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("details/", views.details, name="details"),
    path("success/<int:pk>/", views.success, name="success"),
    path("edit/<int:pk>/", views.updatedetails, name="updatedetails")
]
