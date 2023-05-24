from django.shortcuts import render, redirect
from question.choiceQuestion_models import choiceQuestionForm
from question.compositionQuestion_models import compositionQuestionForm
from question.questionpaper_models import QPForm
from question.models import ExamForm

# Create your views here.

def addQuestion(request):
    return render(request, "question/addQuestion.html")

def addCompositionQuestion(request):
    composition_form_init = compositionQuestionForm()
    if request.method == 'POST':
        composition_form = compositionQuestionForm(request.POST)
        if composition_form.is_valid():
            # 这里可以增加延迟提交，增加教师的选项，这里先忽略
            composition_exam = composition_form.save()
            return redirect("addCompositionQuestion")
    else:
        return render(request, "question/addCompositionQuestion.html", {
            'compositionForm':composition_form_init
            })
    return render(request, "question/addCompositionQuestion.html")

def addChoiceQuestion(request):
    choice_form_init = choiceQuestionForm()
    if request.method == 'POST':
        choice_form = choiceQuestionForm(request.POST)
        if choice_form.is_valid():
            # 这里可以增加延迟提交，增加教师的选项，这里先忽略
            choice_exam = choice_form.save()
            return redirect("addChoiceQuestion")
    else:
        return render(request, "question/addChoiceQuestion.html", {
            'choiceForm':choice_form_init
            })
    return render(request, "question/addChoiceQuestion.html")

def addQuestionPaper(request):
    exam_form_init = QPForm()
    if request.method == 'POST':
        exam_form = QPForm(request.POST)
        if exam_form.is_valid():
            exam = exam_form.save()
            return redirect('addQuestionPaper')
    else:
        return render(request, 'question/addquestionpaper.html', {
            'examform': exam_form_init,
        })
    return render(request, "question/addQuestionPaper.html")

def releaseExams(request):
    exam_form_init = ExamForm()
    if request.method == 'POST':
        exam_form = ExamForm(request.POST)
        if exam_form.is_valid():
            exam = exam_form.save()
            return redirect('releaseExams')
    else:
        return render(request, 'question/releaseExams.html', {
            'examForm': exam_form_init, 
        })
    return render(request, 'question/releaseExams.html')
