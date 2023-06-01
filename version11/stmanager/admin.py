from django.contrib import admin
from .models import User

# Register your models here.
class STManagerUserManager(admin.ModelAdmin):
    list_display = ['username', 'password']

    search_fields = ['username', 'password']

# admin.site.register(User, STManagerUserManager)