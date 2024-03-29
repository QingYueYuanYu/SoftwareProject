# Generated by Django 4.2 on 2023-05-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='choiceQuestion_DB',
            fields=[
                ('qno', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('optionA', models.CharField(max_length=100)),
                ('optionB', models.CharField(max_length=100)),
                ('optionC', models.CharField(max_length=100)),
                ('optionD', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=200)),
                ('max_marks', models.IntegerField(default=0)),
            ],
        ),
    ]
