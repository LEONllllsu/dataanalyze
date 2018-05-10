# _*_ coding: utf-8 _*_
__author__ = 'leonsu'
__date__ = '2018/5/8 23:01'
import xadmin
from .models import UserAddData


class UserAddDataAdmin(object):
    list_display = ['user', 'dataResource', 'add_time']


xadmin.site.register(UserAddData, UserAddDataAdmin)
