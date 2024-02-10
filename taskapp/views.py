from django.shortcuts import render
from taskapp.models import Task

# Create your views here.

def task_list(request):
    task_list = Task.objects.all()
    name  = request.GET.get('name')
    employee  = request.GET.get('employee')
    ordering = request.GET.get('ordering')
    if name:
        task_list = task_list.filter(
            name__icontains=name
        )

    if employee:
        task_list = task_list.filter(
            employee__name__icontains=employee
        )
    ORDERING = [
        'name','deadlite','employee'
    ]
    if ordering and ordering in ORDERING :
        task_list = task_list.order_by(ordering)

    context= {
        "task_list" : task_list
    }
    return render(request,'task_list.html',context)

def task_detail(request,pk):
    context= {
        "task" : Task.objects.get(id=pk)
    }
    return render(request,'task_detail.html',context)
