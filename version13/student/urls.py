from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('student_info/', views.student_info_view),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('payment/', views.payment, name='payment'),
]