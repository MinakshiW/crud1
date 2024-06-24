from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
from .models import User

# Create your views here.

def hview(request):
    return render(request, 'app1/home.html', {})

def uview(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Saved!!!!!')
    return render(request, 'app1/user.html', {'form': form})

def sview(request):
    user = User.objects.all()
    return render(request, 'app1/show.html', {'obj': user})