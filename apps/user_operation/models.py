import os

from django.db import models
from django.contrib.auth import get_user_model

from datetime import datetime

# Create your models here.
User = get_user_model()


class UserAddData(models.Model):
    """
    用户添加数据源
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    dataResource = models.FileField(upload_to="personaldata", verbose_name="上传的数据源")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户添加数据源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.dataResource)
