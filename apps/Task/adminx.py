# _*_ coding: utf-8 _*_
__author__ = 'leonsu'
__date__ = '2018/5/8 23:01'
import xadmin
from .models import Task


class TaskAdmin(object):
    list_display = ['Task_ID', 'user', 'dataResource', 'add_time']


xadmin.site.register(Task, TaskAdmin)
