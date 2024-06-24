from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def hview(request):
    return render(request, 'app1/home.html', {})

def eview(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Added!!!!')
    return render(request, 'app1/emp.html', {'form': form})

def sview(request):
    emp = Employee.objects.all()
    return render(request, 'app1/show.html', {'obj': emp})