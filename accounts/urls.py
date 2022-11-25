from django.urls import path

from . import views

urlpatterns = [
    path("details/", views.details, name="details"),
    path("success/", views.success, name="success"),
    path("edit/<str:pk>/", views.edit, name="edit"),
]
