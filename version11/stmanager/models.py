from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField("账号", max_length=30, unique=True)
    password = models.CharField("密码", max_length=32)

    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return f'{self.username}--{self.password}'

    # 修改表明
    class Meta:
        # 表名：应用名_类名非驼峰
        db_table = 'stmanager_user'
        verbose_name = '管理员'
        verbose_name_plural = '管理员表'
