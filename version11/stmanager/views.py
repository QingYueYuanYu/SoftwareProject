from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import User as ST_User


def login_view(request):
    if request.method == 'GET':
        if 'st_uid' in request.session and 'st_username' in request.session:
            return HttpResponseRedirect('/stmanager/stmanager_info/')
        return render(request, 'stmanager/login.html')
    elif request.method == 'POST':
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验数据
        if not username or not password:
            return HttpResponse('用户名或密码不能为空')
        try:
            user = ST_User.objects.get(username=username)
        except:
            return HttpResponse('用户名或密码错误')
        if user.password != password:
            return HttpResponse('用户名或密码错误')
        # 保存登录状态
        request.session['st_username'] = user.username
        request.session['st_uid'] = user.id
        return HttpResponseRedirect('/stmanager/stmanager_info/')


def login_check(fn):
    def wrap(request, *args, **kwargs):
        if 'st_uid' not in request.session or 'st_username' not in request.session:
            return HttpResponseRedirect('/stmanager/login/')
        return fn(request, *args, **kwargs)

    return wrap


@login_check
def stmanager_info_view(request):
    username = request.session.get('st_username')
    uid = request.session.get('st_uid')
    user = ST_User.objects.get(id=uid)
    # print(username,uid,user,user.id,user.name)

    return render(request, 'stmanager/stmanager_info.html', locals())


def logout_view(request):
    if 'st_uid' not in request.session or 'st_username' not in request.session:
        return HttpResponse('用户还未登录')
    del request.session['st_uid']
    del request.session['st_username']
    return HttpResponseRedirect('/')




def stmanager_info_view1(request):


    return render(request, 'stmanager/stmanager_info1.html',)