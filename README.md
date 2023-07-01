# 环境部署

    1、确保已安装MySql，设置MySql账号为root 密码为123456

    2、创建数据库 create database stinfo charset=utf8;

    3、安装项目需要的包，执行该命令pip install -r requirements.txt  

    4、迁移文件 python manage.py makemigrations                 python manage.py migrate

    5、创建管理员账号 python manage.py createsuperuser

    6、启动django        python manage.py runserver

    7、在浏览器输入 http://127.0.0.1:8000/

# 功能说明

    templates文件夹存放模板
        index.html 主页
        teachae/login.html 老师登录页面
        teacher/register.html 老师注册页面
        teacher/teacher_info.html 老师信息页面
        student/login.html 学生登录页面
        student/register.html 学生注册页面
        student/teacher_info.html 学生信息页面


    static文件夹是存放图片,css,js等静态文件


    media/avatars文件夹存放老师学生头像


    stinfo是主应用文件夹
        settings.py 项目的配置文件
        urls.py 主路由文件
        views.py 中 index_view() 主页的视图函数


    teacher是老师应用文件夹
        migrations文件夹是老师的数据库迁移文件夹
        admin.py 存放老师的自定义模型类
        models.py 存放老师的模型类
        urls.py 老师的路由文件
        views.py 老师的视图函数文件
            login_view()  老师的登录视图函数
            login_check()  老师的登陆状态检测装饰器
            teacher_info_view() 老师的信息页面视图函数
            logout_view() 老师的登出视图函数
            register_view() 老师的注册视图函数


    student是学生应用文件夹
        migrations文件夹是学生的数据库迁移文件夹
        admin.py 存放学生的自定义模型类
        models.py 存放学生的模型类
        urls.py 学生的路由文件
        views.py 学生的视图函数文件
            login_view()  学生的登录视图函数
            login_check()  学生的登陆状态检测装饰器
            teacher_info_view() 学生的信息页面视图函数
            logout_view() 学生的登出视图函数
            register_view() 学生的注册视图函数


    questions是考试应用文件夹
        migrations文件夹是考试的数据库迁移文件夹
        admin.py 存放考试的自定义模型类
        models.py 存放考试的模型类
            choiceQuestion_models.py 存放选择题的模型类
            compositionQuestion_models.py 存放简答题的模型类
            questionpaper_models.py 存放试卷的模型类
        urls.py 试卷的路由文件
        views.py 试卷的视图函数文件
            addQuestion()  添加试卷的主菜单函数
            addChoiceQuestion()  添加选择题的函数
            addCompositionQuestion()  添加简答题的函数
            addQuestionPaper()  添加试卷的函数
            releaseExams()  发布试卷的函数
            checkExams()  学生查看试卷的函数
            answerExams()  学生线上答题的函数
            teacherCheckExams()  老师查看试卷的函数
            scoreExams()  老师阅卷的函数
            checkResults()  学生查看成绩的函数