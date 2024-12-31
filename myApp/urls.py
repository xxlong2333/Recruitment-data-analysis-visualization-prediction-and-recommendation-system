"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myApp import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("salaryChar/", views.salaryChar, name="salaryChar"),
path("logOut/", views.logOut, name="logOut"),
    path("login/", views.login, name="login"),

    path("educationChar/", views.educationChar, name="educationChar"),
    path("registry/", views.registry, name="registry"),
    path("industryChar/", views.industryChar, name="industryChar"),
    path("cityChar/", views.cityChar, name="cityChar"),
    path("tableData/", views.tableData, name="tableData"),
    path("changeInfo/", views.changeInfo, name="changeInfo"),
    path("addHistory/<int:jobId>/", views.addHistory, name="addHistory"),
    path("delHistory/<int:jobId>/", views.delHistory, name="delHistory"),
    path("collectData/", views.collectData, name="collectData"),

    path("titleCloud/", views.titleCloud, name="titleCloud"),

    path("tagCloud/", views.tagCloud, name="tagCloud"),
    path("recommendPage/", views.recommendPage, name="recommendPage"),
    path("predict/", views.predict, name="predict"),

]
