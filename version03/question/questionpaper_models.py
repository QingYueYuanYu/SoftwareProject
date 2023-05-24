from django.db import models
from django.forms import ModelForm
from .choiceQuestion_models import choiceQuestion_DB
from .compositionQuestion_models import compositionQuestion_DB
from django import forms

class Question_Paper(models.Model):
    qPaperTitle = models.CharField(max_length=100)
    choiceQuestions = models.ManyToManyField(choiceQuestion_DB)
    compositionQuestions = models.ManyToManyField(compositionQuestion_DB)

    def __str__(self):
        return f' Question Paper Title :- {self.qPaperTitle}\n'

class QPForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (QPForm,self ).__init__(*args,**kwargs) 
        self.fields['choiceQuestions'].queryset = choiceQuestion_DB.objects.all()
        self.fields['compositionQuestions'].queryset = compositionQuestion_DB.objects.all()

    class Meta:
        model = Question_Paper
        fields = '__all__'
        # exclude = ['professor']
        widgets = {
            'qPaperTitle': forms.TextInput(attrs = {'class':'form-control'})
        }
