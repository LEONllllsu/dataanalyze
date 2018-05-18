import shutil

from django.http import HttpResponse
from django.shortcuts import render
from Task.models import Task
import os
from django import forms


# Create your views here.
class UploadFileForm(forms.Form):
    task_name = forms.CharField(max_length=15)
    task_file = forms.FileField()


def handle_uploaed_file(f, n):
    shutil.copy(f, "D:\\Task\\task" + str(n))


def Task_go(request):
    if request.method == "POST":
        # username = request.session.get('username', '')
        form = UploadFileForm(request.POST, request.FILES)
        TASK = Task.objects.all()
        task_id = 1
        for n in TASK:
            task_id = task_id + 1
        if form.is_valid():
            task = Task()
            task.Task_name = form.cleaned_data['task_name']
            task.task_excel_origin = form.cleaned_data['task_file']
            task.Task_ID = task_id
            task.user_id = 1  # 之后在session里面提取user_id
            os.makedirs("D:\\Task\\task" + str(task_id))
            # File = Task.objects.get(Task_ID=task_id)
            # file_index = str(File.task_excel_origin).replace('/', '\\')
            file_name = form.cleaned_data['task_file'].name
            handle_uploaed_file(
                "C:\\Users\\LEONsu\\PycharmProjects\\untitled\\data_analyze\\personaldata\\" + file_name, task_id)
            task.task_excel_last = "D:\\Task\\task" + str(task_id) + "\\" + str(file_name)
            task.save()

        return render(request, 'newApplication.html')


def show(request):
    return render(request, 'newApplication.html')
