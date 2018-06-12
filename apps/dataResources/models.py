from django.db import models
from datetime import datetime

from users.models import UserProfile
from Task.models import Task


# Create your models here.

class DataResource(models.Model):
    """
    数据源
    """
    DATA_TYPE = (
        (1, "excel"),
        (2, "txt"),
        (3, "csv")
    )
    step1 = models.CharField(max_length=100, verbose_name="源文件名", default="")
    step2 = models.CharField(max_length=100, verbose_name="源json文件", default="")
    step3 = models.CharField(max_length=100, verbose_name="step3文件", default="")
    step4 = models.CharField(max_length=100, verbose_name="step4文件", default="")
    step5 = models.CharField(max_length=100, verbose_name="step5文件", default="")
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE, default="")
    Task_id = models.ForeignKey(Task, verbose_name="任务编号", on_delete=models.CASCADE, default="")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "数据源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.DataResources
