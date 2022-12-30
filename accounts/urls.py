from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("details/", views.details, name="details"),
    # path("success/<str:pk>/", views.success, name="success"),
    # path("update/<str:pk>/", views.updatedetails, name="updatedetails"),
    path("books/", views.books, name="book"),
    path("test/", views.test, name="test"),
    path("test1/", views.test1, name="test1"),
    path("uploadedby/", views.uploadedby, name="uploadedby")
]
