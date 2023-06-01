# Generated by Django 4.2.1 on 2023-05-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=30, unique=True, verbose_name="账号"),
                ),
                ("password", models.CharField(max_length=32, verbose_name="密码")),
                ("is_active", models.BooleanField(default=True, verbose_name="是否激活")),
                (
                    "created_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_time",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
            ],
            options={
                "verbose_name": "管理员",
                "verbose_name_plural": "管理员表",
                "db_table": "stmanager_user",
            },
        ),
    ]