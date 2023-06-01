from django.contrib import admin
from .models import User

# Register your models here.
class TeacherUserManager(admin.ModelAdmin):
    list_display = ['name', 'username', 'password', 'gender', 'id_number', 'avatar']
    list_filter = ['gender']
    search_fields = ['name', 'username', 'password', 'gender', 'id_number', 'avatar']


admin.site.register(User, TeacherUserManager)
