from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime


# Create your models here.

class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=20, verbose_name="名字", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    gender = models.CharField(max_length=6, choices=(("female", "女"), ("male", "男")), default="male", verbose_name="性别")
    email = models.CharField(max_length=30, null=True, blank=True, verbose_name="邮箱")
    company = models.CharField(max_length=100, null=True, blank=True, verbose_name="公司")
    career = models.CharField(max_length=20, choices=(("student", "学生"), ("others", "其他")), default="student")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
     短信验证码
    """
    code = models.CharField(max_length=6, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
