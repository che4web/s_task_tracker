from django.shortcuts import render
from taskapp.models import Task

# Create your views here.

def task_list(request):
    context= {
        "task_list" : Task.objects.all()
    }
    return render(request,'task_list.html',context)

def task_detail(request,pk):
    context= {
        "task" : Task.objects.get(id=pk)
    }
    return render(request,'task_detail.html',context)
