from django.contrib import admin

# Register your models her

from .models import CustomerUser,EmailCode
admin.site.register([CustomerUser,EmailCode])