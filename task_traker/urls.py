"""
URL configuration for task_traker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from taskapp.views import task_list,task_detail,task_create
from employeeapp.views import EmployeeListView,EmployeeDetailView

urlpatterns = [
    path('', task_list),
    path('task/<int:pk>/', task_detail),
    path('task/create', task_create),
    path('employee/', EmployeeListView.as_view()),
    path('employee/<int:pk>/', EmployeeDetailView.as_view()),
    path('admin/', admin.site.urls),
]
