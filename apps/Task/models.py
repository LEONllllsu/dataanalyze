from django.db import models

from django.contrib.auth import get_user_model

from datetime import datetime

# Create your models here.
User = get_user_model()


class Task(models.Model):
    """
    任务
    """
    Task_name = models.CharField(max_length=15, verbose_name="任务名", default="")
    Task_ID = models.IntegerField(verbose_name="task_id")
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    task_excel_origin = models.FileField(upload_to="personaldata", verbose_name="上传的初始数据源")
    task_excel_last = models.CharField(max_length=100, verbose_name="用户操作后的数据源", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "添加任务"
        verbose_name_plural = verbose_name
