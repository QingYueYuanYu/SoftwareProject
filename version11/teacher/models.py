from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField("姓名", max_length=32)
    gender = models.CharField("性别", max_length=10)
    id_number = models.CharField("身份证号", max_length=20)
    avatar = models.ImageField("头像", upload_to='avatars')
    username = models.CharField("账号", max_length=30, unique=True)
    password = models.CharField("密码", max_length=32)

    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return f'{self.name}'

    # 修改表明
    class Meta:
        # 表名：应用名_类名非驼峰
        db_table = 'teacher_user'
        verbose_name = '老师'
        verbose_name_plural = '老师表'
