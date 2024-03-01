from django.contrib import messages
from django.shortcuts import render, redirect

from Employee.forms import EmployeeForm


# Create your views here.


def employee_form(request):
    form = EmployeeForm()
    if request.method == 'GET':  # takes the records and populates on url, how url chrome behaves
        form = EmployeeForm()
        return render(request, 'employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Employee')
            return redirect('employee_form')


def employee_list(request):
    return render(request, 'employee_list.html')
