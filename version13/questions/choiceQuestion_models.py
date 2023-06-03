from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class choiceQuestion_DB(models.Model):
    qno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)
    max_marks = models.IntegerField(default=0)

    def __str__(self):
        return f'\t \t     Question No.{self.qno}: {self.question} \t\t\n Options: \tA. {self.optionA} \n\tB.{self.optionB} \n\tC.{self.optionC} \n\tD.{self.optionD} '


class choiceQuestionForm(ModelForm):
    class Meta:
        model = choiceQuestion_DB
        fields = '__all__'
        exclude = ['qno']
        widgets = {
            'question': forms.TextInput(attrs = {'class':'form-control'}),
            'optionA': forms.TextInput(attrs = {'class':'form-control'}),
            'optionB': forms.TextInput(attrs = {'class':'form-control'}),
            'optionC': forms.TextInput(attrs = {'class':'form-control'}),
            'optionD': forms.TextInput(attrs = {'class':'form-control'}),
            'answer': forms.TextInput(attrs = {'class':'form-control'}),
            'max_marks': forms.NumberInput(attrs = {'class':'form-control'}),
        }