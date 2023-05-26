# Generated by Django 4.2 on 2023-05-24 12:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_exam_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu_ChoiceQuestion',
            fields=[
                ('choicequestion_db_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question.choicequestion_db')),
                ('choice', models.CharField(default='E', max_length=3)),
            ],
            bases=('question.choicequestion_db',),
        ),
        migrations.CreateModel(
            name='Stu_CompositionQuestion',
            fields=[
                ('compositionquestion_db_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question.compositionquestion_db')),
                ('translation_answer', models.CharField(default='', max_length=500)),
                ('composition_answer', models.CharField(default='', max_length=500)),
            ],
            bases=('question.compositionquestion_db',),
        ),
        migrations.CreateModel(
            name='StuExam_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examname', models.CharField(max_length=100)),
                ('choice_score', models.IntegerField(default=0)),
                ('composition_score', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
                ('completed', models.IntegerField(default=0)),
                ('choice_questions', models.ManyToManyField(to='question.stu_choicequestion')),
                ('composition_questions', models.ManyToManyField(to='question.stu_compositionquestion')),
                ('qpaper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='question.question_paper')),
            ],
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 20, 34, 44, 816858)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 20, 34, 44, 815859)),
        ),
        migrations.CreateModel(
            name='StuResults_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exams', models.ManyToManyField(to='question.stuexam_db')),
            ],
        ),
    ]
