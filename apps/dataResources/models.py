from django.db import models
from datetime import datetime

from user_operation.models import UserAddData


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
    DataResources = models.ForeignKey(UserAddData, verbose_name="数据源", on_delete=models.CASCADE)
    category = models.IntegerField(choices=DATA_TYPE, verbose_name="数据类别")
    name = models.CharField(max_length=30, verbose_name="名字")
    data_id = models.CharField(max_length=30, verbose_name="数据ID")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "数据源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.DataResources
