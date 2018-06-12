"""data_analyze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

import xadmin
from apps.Task.views import Task_go
from apps.Task.views import show
from users.views import UsersListViewSet
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
router.register('users',  UsersListViewSet)




urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('task_go', Task_go, name='go_task'),
    path('show', show),
    # path('2json', excel2json2.as_view(), name='2json')
    url(r'^', include(router.urls)),

]
