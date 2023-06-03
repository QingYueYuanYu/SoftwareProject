from django.shortcuts import render, redirect
from django.http import HttpResponse
from questions.choiceQuestion_models import choiceQuestionForm, choiceQuestion_DB
from questions.compositionQuestion_models import compositionQuestionForm, compositionQuestion_DB
from questions.questionpaper_models import QPForm, Question_Paper
from questions.models import Exam_Model, ExamForm, StuExam_DB, Stu_ChoiceQuestion, Stu_CompositionQuestion, StuResults_DB
from django.contrib import messages

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
            messages.success(request, "提交成功.")
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
            messages.success(request, "提交成功.")
            return redirect("addChoiceQuestion")
    else:
        return render(request, "question/addChoiceQuestion.html", {
            'choiceForm':choice_form_init
            })
    return render(request, "question/addChoiceQuestion.html")

def addQuestionPaper(request):
    if request.method == 'POST':
        # print(request.POST)
        # print("--------------")
        # qPaperTitle = request.POST.get("qPaperTitle")
        # choiceQuestionList = request.POST.getlist("choiceQuestions")
        # compositionQuestionList = request.POST.get("compositionQuestions")
        # examChoiceQuestionsList = choiceQuestion_DB.objects.filter(qno__in=choiceQuestionList)
        # examCompositionQuestionList = compositionQuestion_DB.objects.filter(qno=compositionQuestionList)
        exam_form_init = Question_Paper()
        qPaperTitle = request.POST.get("qPaperTitle")
        choiceQuestionList = request.POST.getlist("choiceQuestions")
        compositionQuestionList = request.POST.get("compositionQuestions")
        examChoiceQuestionsList = choiceQuestion_DB.objects.filter(qno__in=choiceQuestionList)
        examCompositionQuestionsList = compositionQuestion_DB.objects.filter(qno=compositionQuestionList)
        exam_form_init.qPaperTitle = qPaperTitle
        exam_form_init.save()
        for examChoiceQuestion in examChoiceQuestionsList:
            # print("-------------------------")
            # print(examChoiceQuestion.qno)
            # choiceQues = choiceQuestion_DB.objects.filter(qno=examChoiceQuestion.qno)
            exam_form_init.choiceQuestions.add(examChoiceQuestion.qno)
            exam_form_init.save()
        for examCompositionQuestion in examCompositionQuestionsList:
            # compositionQues = compositionQuestion_DB.objects.filter(qno=examCompositionQuestion.qno)
            exam_form_init.compositionQuestions.add(examCompositionQuestion.qno)
            exam_form_init.save()
            messages.success(request, "提交成功.")
        return redirect('addQuestionPaper')
        # print("choiceQuestionList: ", choiceQuestionList)
        # print("ExamChoceQuestionList: ", examChoiceQuestionsList)
        # print("ExamCompositionQuestionList: ", examCompositionQuestionsList)
        # request.POST.get("choiceQuestion")
        # print("--------------------")
        # exam_form = QPForm(request.POST)
        # print(exam_form)
        # if exam_form.is_valid():
        #     exam = exam_form.save()
        #     print("Success")
        #     return redirect('addQuestionPaper')
        # else:
        #     print("Fail")
    else:
        exam_form_init = QPForm()
        return render(request, 'question/addQuestionPaper.html', {
            'examform': exam_form_init,
        })
    return render(request, "question/addQuestionPaper.html")

def releaseExams(request):
    exam_form_init = ExamForm()
    if request.method == 'POST':
        exam_form = ExamForm(request.POST)
        if exam_form.is_valid():
            exam = exam_form.save()
            messages.success(request, "提交成功.")
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
        print("--------------------------------------")
        print(paper)
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
            max_m = choice_list_i[i].max_marks
            ans = request.POST.get(ques.question, False)
            if not ans:
                ans = "E"
            ques.choice = ans
            ques.save()
            if ans.lower() == ques.answer.lower() or ans == ques.answer:
                examChoiceScore = examChoiceScore + max_m
            i+=1

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
        stuExam.choice_score = examChoiceScore
        stuExam.save()
        # stu = StuExam_DB.objects.filter(examname=examMain.name)  
        # results = StuResults_DB.objects.get_or_create()[0]
        # results.exams.add(stu[0])
        # results.save()
        js = """
        <div id="btn_area"></div>
        <script>
        var ms = 3;// 定义全局变量,几秒之后自动跳转
        function returnLogin(){
            if(ms>0){
                document.getElementById("btn_area").innerHTML="<span id='loginTip' class='ok_txt2'>提交成功！ "+ms+" 秒后将自动关闭该界面...</span>";
            }else{
                window.close();
            }
            ms--;// 每调用一次减减
        }
        setInterval(returnLogin,1000);// 第二个参数单位毫秒,此处意思是每间隔1秒调用一次returnLogin方法
        </script>
        """

        return HttpResponse(js)
        # return redirect('checkExams')

def teacherCheckExams(request):
    exams = Exam_Model.objects.all()
    list_of_completed = []
    list_of_uncompleted = []
    for exam in exams:
        # 这里已经做过的试卷会重新显示，回头再看吧
        # if StuExam_DB.objects.get(examname=exam.name).completed == 1:
            # list_of_completed.append(exam)
        # else:
        list_of_uncompleted.append(exam)
    return render(request,'question/teacherCheckExams.html',{
        'exams':list_of_uncompleted,
        'completed':list_of_completed
    })

def scoreExams(request, id):
    if request.method == 'GET':
        exam = Exam_Model.objects.get(pk=id)
        stuExam = StuExam_DB.objects.get(examname=exam.name)
        composition_question = exam.question_paper.compositionQuestions.all()[0]
        composition_answer = stuExam.composition_questions.all()[0]
        # print("---------------------------------------")
        # print("composition_question:")
        # print(composition_question)
        # print("---------------------------------------")
        # print("composition_answer")
        # print(composition_answer)
        context = {
            "exam":exam,
            "composition_question":composition_question,
            "composition_answer":composition_answer
        }
        return render(request,'question/scoreExam.html',context)
    
    elif request.method == 'POST':
        paper = request.POST['paper']
        examMain = Exam_Model.objects.get(name = paper)
        stuExam = StuExam_DB.objects.get(examname=paper, qpaper = examMain.question_paper)
        
        choice_score = stuExam.choice_score
        composition_score = int(request.POST["translation_score"]) + int(request.POST["composition_score"])
        stuExam.composition_score = composition_score
        stuExam.total_score = choice_score + composition_score
        stuExam.save()
        js = """
        <div id="btn_area"></div>
        <script>
        var ms = 3;// 定义全局变量,几秒之后自动跳转
        function returnLogin(){
            if(ms>0){
                document.getElementById("btn_area").innerHTML="<span id='loginTip' class='ok_txt2'>提交成功！ "+ms+" 秒后将自动关闭该界面...</span>";
            }else{
                window.close();
            }
            ms--;// 每调用一次减减
        }
        setInterval(returnLogin,1000);// 第二个参数单位毫秒,此处意思是每间隔1秒调用一次returnLogin方法
        </script>
        """

        return HttpResponse(js)
        # return redirect('teacherCheckExams')

def checkResults(request):
    stuExams = StuExam_DB.objects.all()
    return render(request,'question/checkResults.html',{
        'exams':stuExams
    })