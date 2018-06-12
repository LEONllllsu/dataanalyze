# _*_ coding: utf-8 _*_
__author__ = 'leonsu'
__date__ = '2018/6/5 14:19'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)