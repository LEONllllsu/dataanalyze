# _*_ coding: utf-8 _*_
__author__ = 'leonsu'
__date__ = '2018/5/8 23:01'
import xadmin
from .models import DataResource


class DataResourceAdmin(object):
    list_display = ['DataResources', 'category', 'name', 'data_id', 'add_time']


xadmin.site.register(DataResource, DataResourceAdmin)
