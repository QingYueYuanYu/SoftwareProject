from django.contrib import admin
from .models import User

# Register your models here.
class StuUserManager(admin.ModelAdmin):
    list_display = ['name', 'username', 'password', 'gender', 'id_number', 'avatar', 'birthdate', 'school', 'region']
    # list_display_links = ['id', 'title']
    list_filter = ['gender', 'school', 'region']
    search_fields = ['name', 'username', 'password', 'gender', 'id_number', 'avatar', 'birthdate', 'school', 'region']
    # list_editable = ['price','market_price','is_active']

admin.site.register(User, StuUserManager)

from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)