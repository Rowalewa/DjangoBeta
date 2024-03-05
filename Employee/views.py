from django.contrib import messages
from django.shortcuts import render, redirect

from Employee.forms import EmployeeForm
from Employee.models import Employee


# Create your views here.


def employee_form(request, id=0):
    form = EmployeeForm()
    if request.method == 'GET':  # takes the records and populates on url, how url chrome behaves
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_form.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Employee')
            return redirect('employee_list')


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_list.html', context)


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()  # inbuilt for deletion in django.
    return redirect('employee_list')
