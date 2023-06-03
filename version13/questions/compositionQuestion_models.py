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
        return f'Question No.{self.qno}: \nTranslation: \n {self.translation_description} \nComposition: \n {self.composition_description}'

class compositionQuestionForm(ModelForm):
    class Meta:
        model = compositionQuestion_DB
        fields = '__all__'
        exclude = ['qno']
        # 这个阅读题的宽度问题回头还得再改一改
        widgets = {
            'translation_description': forms.Textarea(attrs = {'class':'form-control'}),
            'max_translation_marks': forms.TextInput(attrs = {'class':'form-control'}),
            'composition_description': forms.Textarea(attrs = {'class':'form-control'}),
            'max_composition_marks': forms.TextInput(attrs = {'class':'form-control'}),
        }