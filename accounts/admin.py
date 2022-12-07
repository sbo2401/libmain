from django.contrib import admin

from accounts.models import *
from accounts.forms import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdmin(UserAdmin):
    model = User
    list_display=["username", "email", "first_name", "last_name", "is_superuser","is_active","is_staff",]

@admin.register(UserProfile)
class Details(admin.ModelAdmin):
    list_display = ("username",)
admin.site.register(User ,UserAdmin)
admin.site.register(Books)