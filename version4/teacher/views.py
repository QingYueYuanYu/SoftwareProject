from django.shortcuts import render

# Create your views here.
def teacherIndex(request):
    return render(request, "teacher/teacherIndex.html")


    