from django import forms
from myapp.models import Student
from myapp.models import Employee


class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name:", max_length=50)
    lastname = forms.CharField(label="Enter last name:", max_length=100)
    email=forms.EmailField(label="Enter Email")
    file=forms.FileField()

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
