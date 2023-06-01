from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('stmanager_info/', views.stmanager_info_view),
    path('stmanager_info1/', views.stmanager_info_view1),
    path('logout/', views.logout_view),
]