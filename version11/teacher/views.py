from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import User


def login_view(request):
    if request.method == 'GET':
        if 't_uid' in request.session and 't_username' in request.session:
            return HttpResponseRedirect('/teacher/teacher_info/')
        return render(request, 'teacher/login.html')
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
        request.session['t_username'] = user.username
        request.session['t_uid'] = user.id
        return HttpResponseRedirect('/teacher/teacher_info/')


def login_check(fn):
    def wrap(request, *args, **kwargs):
        if 't_uid' not in request.session or 't_username' not in request.session:
            return HttpResponseRedirect('/teacher/login/')
        return fn(request, *args, **kwargs)

    return wrap


@login_check
def teacher_info_view(request):
    username = request.session.get('t_username')
    uid = request.session.get('t_uid')
    user = User.objects.get(id=uid)
    # print(username,uid,user,user.id,user.name)

    return render(request, 'teacher/teacher_info.html', locals())


def logout_view(request):
    if 't_uid' not in request.session or 't_username' not in request.session:
        return HttpResponse('用户还未登录')
    del request.session['t_uid']
    del request.session['t_username']
    return HttpResponseRedirect('/')

def register_view(request):
    if request.method == 'GET':
        return render(request, 'teacher/register.html')
    elif request.method == 'POST':
        # 获取数据
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        avatar = request.FILES['avatar']
        id_number = request.POST.get('id_number')
        # print('注册信息--->',username,password1,password2,name,gender,avatar,id_number)
        # 校验数据
        if password1 != password2:
            return HttpResponse('两次密码不一致')
        if not username or not password1:
            return HttpResponse('用户名或密码不能为空')
        if User.objects.filter(username=username):
            return HttpResponse('用户名已存在')
        # 保存数据
        User.objects.create(username=username, password=password1, name=name, gender=gender, avatar=avatar, id_number=id_number)

        js = """
        <div id="btn_area"></div>
        <script>
        var ms = 3;// 定义全局变量,几秒之后自动跳转
        function returnLogin(){
            if(ms>0){
                document.getElementById("btn_area").innerHTML="<span id='loginTip' class='ok_txt2'>恭喜注册成功！ "+ms+" 秒后将自动跳转至登录界面...</span><a href='login.html'>直接跳转</a>";
            }else{
                window.location.href="/teacher/login/";
            }
            ms--;// 每调用一次减减
        }
        setInterval(returnLogin,1000);// 第二个参数单位毫秒,此处意思是每间隔1秒调用一次returnLogin方法
        </script>
        """

        return HttpResponse(js)
