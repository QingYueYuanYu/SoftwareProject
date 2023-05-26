from django.shortcuts import render, redirect
from question.choiceQuestion_models import choiceQuestionForm
from question.compositionQuestion_models import compositionQuestionForm
from question.questionpaper_models import QPForm
from question.models import Exam_Model, ExamForm, StuExam_DB, Stu_ChoiceQuestion, Stu_CompositionQuestion, StuResults_DB


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

def checkExams(request):
    exams = Exam_Model.objects.all()
    list_of_completed = []
    list_of_uncompleted = []
    for exam in exams:
        # 这里已经做过的试卷会重新显示，回头再看吧
        # if StuExam_DB.objects.get(examname=exam.name).completed == 1:
            # list_of_completed.append(exam)
        # else:
        list_of_uncompleted.append(exam)
    return render(request,'question/checkExams.html',{
        'exams':list_of_uncompleted,
        'completed':list_of_completed
    })

def convert(seconds):
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    min += hour*60
    return "%02d:%02d" % (min, sec) 

def answerExams(request, id):
    if request.method == 'GET':
        exam = Exam_Model.objects.get(pk=id)
        time_delta = exam.end_time - exam.start_time
        time = convert(time_delta.seconds)
        time = time.split(":")
        mins = time[0]
        secs = time[1]
        context = {
            "exam":exam,
            "choice_question_list":exam.question_paper.choiceQuestions.all(),
            "composition_question_list":exam.question_paper.compositionQuestions.all(),
            "secs":secs,
            "mins":mins
        }
        return render(request,'question/answerExam.html',context)
    
    elif request.method == 'POST':
        paper = request.POST['paper']
        examMain = Exam_Model.objects.get(name = paper)
        stuExam = StuExam_DB.objects.get_or_create(examname=paper, qpaper = examMain.question_paper)[0]
        
        qPaper = examMain.question_paper
        stuExam.qpaper = qPaper
         
        # qPaperQuestionsList = examMain.question_paper.questions.all()
        qPaperChoiceQuestionsList = examMain.question_paper.choiceQuestions.all()
        qPaperCompositionQuestionList = examMain.question_paper.compositionQuestions.all()
        for ques in qPaperChoiceQuestionsList:
            student_choice_question = Stu_ChoiceQuestion(question=ques.question, optionA=ques.optionA, optionB=ques.optionB,optionC=ques.optionC, optionD=ques.optionD,
            answer=ques.answer)
            student_choice_question.save()
            stuExam.choice_questions.add(student_choice_question)
            stuExam.save()

        for ques in qPaperCompositionQuestionList:
            student_composition_question = Stu_CompositionQuestion(translation_description=ques.translation_description,
            composition_description=ques.composition_description)
            student_composition_question.save()
            stuExam.composition_questions.add(student_composition_question)
            stuExam.save()

        stuExam.completed = 1
        stuExam.save()
        examQuestionsList = StuExam_DB.objects.filter(examname=paper,qpaper=examMain.question_paper)[0]
        #examQuestionsList = stuExam.questions.all()
        examChoiceScore = 0
        choice_list_i = examMain.question_paper.choiceQuestions.all()
        choice_queslist = examQuestionsList.choice_questions.all()
        i = 0
        # 这里只是保存了答卷的数据
        for j in range(choice_list_i.count()):
            ques = choice_queslist[j]
            # max_m = choice_list_i[i].max_marks
            ans = request.POST.get(ques.question, False)
            if not ans:
                ans = "E"
            ques.choice = ans
            ques.save()
            # if ans.lower() == ques.answer.lower() or ans == ques.answer:
                # examChoiceScore = examChoiceScore + max_m
            # i+=1

        composition_list_i = examMain.question_paper.compositionQuestions.all()
        composition_queslist = examQuestionsList.composition_questions.all()
        for j in range(composition_list_i.count()):
            ques = composition_queslist[j]
            translation_answer = request.POST.get(ques.translation_description, False)
            composition_answer = request.POST.get(ques.composition_description, False)
            if not translation_answer:
                translation_answer = "Not Answer"
            if not composition_answer:
                composition_answer = "Not Answer"
            print("Tranlation_Answer:", translation_answer)
            print("Composition_Answer:", composition_answer)
            ques.translation_answer = translation_answer
            ques.composition_answer = composition_answer
            ques.save()
        # 最后的结果保存放在手动阅卷之后
        # stuExam.choice_score = examChoiceScore
        stuExam.save()
        # stu = StuExam_DB.objects.filter(examname=examMain.name)  
        # results = StuResults_DB.objects.get_or_create()[0]
        # results.exams.add(stu[0])
        # results.save()
        return redirect('checkExams')