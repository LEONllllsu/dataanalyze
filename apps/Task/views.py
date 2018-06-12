import shutil

from django.http import HttpResponse
from django.shortcuts import render
from Task.models import Task
import os
from django import forms
from .excel2json import readExcel


# Create your views here.
class UploadFileForm(forms.Form):
    task_name = forms.CharField(max_length=15)
    task_file = forms.FileField()


def handle_uploaed_file(f, n):
    shutil.copy(f, "D:\\Task\\task" + str(n) + "\\Data")


def mkdir(floder):
    os.mkdir(floder)
    os.mkdir(floder + "\\Data")
    os.mkdir(floder + "\\Publish")
    os.mkdir(floder + "\\Log")


def Task_go(request):
    if request.method == "POST":
        # username = request.session.get('username', '')
        form = UploadFileForm(request.POST, request.FILES)
        TASK = Task.objects.all()

        task_id = 1
        for n in TASK:
            task_id = task_id + 1

        Task_home = ['C', 'D', 'E', 'F']
        Task_floder = Task_home[1] + ":\Task\\task" + str(task_id)

        if form.is_valid():
            task = Task()
            task.Task_name = form.cleaned_data['task_name']
            task.task_excel_origin = form.cleaned_data['task_file']
            task.Task_ID = task_id
            task.Task_Home = Task_home[1]
            task.Task_Folder = Task_floder
            task.Task_Folder_name = 'task' + str(task_id)
            task.user_id = 1  # 之后在session里面提取user_id
            task.save()

            mkdir(Task_floder)

            # File = Task.objects.get(Task_ID=task_id)
            # file_index = str(File.task_excel_origin).replace('/', '\\')

            File = Task.objects.get(Task_ID=task_id)

            file_floder = str(File.task_excel_origin)
            # file_floder_new = file_floder.replace('/', '\\', 1)
            origin_index = "C:\\Users\\LEONsu\\PycharmProjects\\untitled\\data_analyze\\" + file_floder
            handle_uploaed_file(origin_index, task_id)

            readExcel(Task_floder + "\\Data\\", origin_index, 1, task_id)

            # task.task_excel_last = "D:\\Task\\task" + str(task_id) + "\\" + str(file_name)
            # Task.objects.create(task_excel_last=task.task_excel_last)

        return render(request, 'newApplication.html')


def show(request):
    return render(request, 'newApplication.html')
