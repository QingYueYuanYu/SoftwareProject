from django.shortcuts import render, redirect
from question.choiceQuestion_models import choiceQuestionForm

# Create your views here.

def addQuestion(request):
    return render(request, "question/addQuestion.html")

def addCompositionQuestion(request):
    return render(request, "question/addCompositionQuestion.html")

def addChoiceQuestion(request):
    # 暂时只显示选择题
    choice_form_init = choiceQuestionForm()
    if request.method == 'POST':
        choice_form = choiceQuestionForm(request.POST)
        if choice_form.is_valid():
            # 这里可以增加延迟提交，增加教师的选项，这里先忽略
            choice_exam = choice_form.save()
            return redirect("addQuestion")
    else:
        return render(request, "question/addQuestion.html", {
            'choiceForm':choice_form_init
            })
    return render(request, "question/addChoiceQuestion.html")