from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django import forms
from .questionpaper_models import Question_Paper
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