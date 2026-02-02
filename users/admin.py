from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UsersAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

admin.site.register(User, UsersAdmin)
