from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class compositionQuestion_DB(models.Model):
    qno = models.AutoField(primary_key=True)
    translation_description = models.CharField(max_length=500)
    max_translation_marks = models.IntegerField(default=0)
    composition_description = models.CharField(max_length=500)
    max_composition_marks = models.IntegerField(default=0)

    def __str__(self):
        return f'Question No.{self.qno}: \nTranslation Description: \n {self.translation_description} \nComposition Description: \n {self.composition_description}'


class compositionQuestionForm(ModelForm):
    class Meta:
        model = compositionQuestion_DB
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