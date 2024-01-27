from django.shortcuts import render
from employeeapp.models import Employee
from django.views.generic import ListView,DetailView


class EmployeeListView(ListView):
    model =Employee

class EmployeeDetailView(DetailView):
    model = Employee

# Create your views here.

#def employee_list(request):
#    context= {
#        "employee_list" : Employee.objects.all()
#    }
#    return render(request,'employee_list.html',context)

#def employee_detail(request,pk):
#    context= {
#        "employee" : Employee.objects.get(id=pk)
#    }
#    return render(request,'employee_detail.html',context)



