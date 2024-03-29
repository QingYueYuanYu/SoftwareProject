"""
URL configuration for CET6_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('addQuestion/', views.addQuestion, name='addQuestion'),
    path('addChoiceQuestion/', views.addChoiceQuestion, name='addChoiceQuestion'),
    path('addCompositionQuestion/', views.addCompositionQuestion, name='addCompositionQuestion'),
    path('addQuestionPaper/', views.addQuestionPaper, name='addQuestionPaper'),
    path('releaseExams/', views.releaseExams, name='releaseExams'),
    path('checkExams/', views.checkExams, name='checkExams'),
    path('answerExams/<int:id>', views.answerExams, name='answerExams'),
    path('teacherCheckExams/', views.teacherCheckExams, name='teacherCheckExams'),
    path('scoreExams/<int:id>', views.scoreExams, name="scoreExams"),
    path('checkResults/', views.checkResults, name="checkResults"),
]
