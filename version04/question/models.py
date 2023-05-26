from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django import forms
from .questionpaper_models import Question_Paper
from .choiceQuestion_models import choiceQuestion_DB
from .compositionQuestion_models import compositionQuestion_DB
# Create your models here.
class Exam_Model(models.Model):
    name = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    question_paper = models.ForeignKey(Question_Paper, on_delete=models.CASCADE, related_name='exams')
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

class ExamForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (ExamForm,self ).__init__(*args,**kwargs) 
        self.fields['question_paper'].queryset = Question_Paper.objects.all()

    class Meta:
        model = Exam_Model
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'total_marks' : forms.NumberInput(attrs = {'class':'form-control'}),
            'start_time': forms.DateTimeInput(attrs = {'class':'form-control'}),
            'end_time': forms.DateTimeInput(attrs = {'class':'form-control'})
        }

# 暂时都放在question里面吧
class Stu_ChoiceQuestion(choiceQuestion_DB):

    choice = models.CharField(max_length=3, default="E")

    def __str__(self):
        return  str(self.qno) +"-Stu_ChoiceQuestionDB"

class Stu_CompositionQuestion(compositionQuestion_DB):

    translation_answer = models.CharField(max_length=500, default="")

    composition_answer = models.CharField(max_length=500, default="")

    def __str__(self):
        return str(self.qno) +"-Stu_CompositionQuestionDB"

class StuExam_DB(models.Model):
    examname = models.CharField(max_length=100)
    qpaper = models.ForeignKey(Question_Paper, on_delete=models.CASCADE, null=True)
    choice_questions = models.ManyToManyField(Stu_ChoiceQuestion)
    composition_questions = models.ManyToManyField(Stu_CompositionQuestion)
    choice_score = models.IntegerField(default=0)
    composition_score = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return str(self.examname) + " " + str(self.qpaper.qPaperTitle) + "-StuExam_DB"

class StuResults_DB(models.Model):
    exams = models.ManyToManyField(StuExam_DB)

    def __str__(self):
        return " -StuResults_DB"
