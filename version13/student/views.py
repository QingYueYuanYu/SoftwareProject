from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import User
from django.contrib import auth
from django.contrib import messages


def login_view(request):
    if request.method == 'GET':
        if 's_uid' in request.session and 's_username' in request.session:
            return HttpResponseRedirect('/student/student_info/')
        return render(request, 'student/login.html')
    elif request.method == 'POST':
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验数据
        if not username or not password:
            return HttpResponse('用户名或密码不能为空')
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('用户名或密码错误')
        if user.password != password:
            return HttpResponse('用户名或密码错误')
        # 保存登录状态
        request.session['s_username'] = user.username
        request.session['s_uid'] = user.id
        return HttpResponseRedirect('/student/student_info/')


def login_check(fn):
    def wrap(request, *args, **kwargs):
        if 's_uid' not in request.session or 's_username' not in request.session:
            return HttpResponseRedirect('/student/login/')
        return fn(request, *args, **kwargs)

    return wrap


@login_check
def student_info_view(request):
    username = request.session.get('s_username')
    uid = request.session.get('s_uid')
    user = User.objects.get(id=uid)
    # print(username,uid,user,user.id,user.name)

    return render(request, 'student/student_info.html', locals())


def payment(request):
    if request.method == "GET":
        return render(request, 'student/payment.html')
    elif request.method == "POST":
        username=request.user.username
        messages.success(request,username + "缴费成功.")
        return render(request,'student/payment.html')

def logout_view(request):
    if 's_uid' not in request.session or 's_username' not in request.session:
        return HttpResponse('用户还未登录')
    del request.session['s_uid']
    del request.session['s_username']
    return HttpResponseRedirect('/')

def register_view(request):
    if request.method == 'GET':
        return render(request, 'student/register.html')
    elif request.method == 'POST':
        # 获取数据
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        avatar = request.FILES['avatar']
        id_number = request.POST.get('id_number')
        birthdate = request.POST.get('birthdate')
        school = request.POST.get('school')
        region = request.POST.get('region')
        # print('注册信息--->',username,password1,password2,name,gender,avatar,id_number,birthdate,school,region)
        # 校验数据
        if password1 != password2:
            return HttpResponse('两次密码不一致')
        if not username or not password1:
            return HttpResponse('用户名或密码不能为空')
        if User.objects.filter(username=username):
            return HttpResponse('用户名已存在')
        # 保存数据
        User.objects.create(username=username, password=password1, name=name, gender=gender, avatar=avatar, id_number=id_number, birthdate=birthdate, school=school, region=region)

        js = """
        <div id="btn_area"></div>
        <script>
        var ms = 3;// 定义全局变量,几秒之后自动跳转
        function returnLogin(){
            if(ms>0){
                document.getElementById("btn_area").innerHTML="<span id='loginTip' class='ok_txt2'>恭喜注册成功！ "+ms+" 秒后将自动跳转至登录界面...</span><a href='login.html'>直接跳转</a>";
            }else{
                window.location.href="/student/login/";
            }
            ms--;// 每调用一次减减
        }
        setInterval(returnLogin,1000);// 第二个参数单位毫秒,此处意思是每间隔1秒调用一次returnLogin方法
        </script>
        """

        return HttpResponse(js)
