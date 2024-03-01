from django import forms
from Employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'emp_code', 'mobile_no', 'position']