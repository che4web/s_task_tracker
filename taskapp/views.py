from django.shortcuts import render
from taskapp.models import Task
from taskapp.forms import TaskSearchForm

# Create your views here.

def task_list(request):
    task_list = Task.objects.all()
    name  = request.GET.get('name')

    form = TaskSearchForm(request.GET)
    print('from request:',request.GET.get('deadlite'), type(request.GET.get('deadlite')))
    if form.is_valid():

        employee  = form.cleaned_data['employee']
        name= form.cleaned_data['name']
        print('from form:',
              form.cleaned_data['deadlite'],
              type(form.cleaned_data['deadlite'])
              )
        if name:
            task_list = task_list.filter(
                name__icontains=name
            )

        if employee:
            task_list = task_list.filter(
                employee__name__icontains=employee
            )
    context= {
        "task_list" : task_list,
        "form":form,
    }
    return render(request,'task_list.html',context)



def task_detail(request,pk):
    context= {
        "task" : Task.objects.get(id=pk)
    }
    return render(request,'task_detail.html',context)
