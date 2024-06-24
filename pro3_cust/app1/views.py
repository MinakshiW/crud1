from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

# Create your views here.
def hview(request):
    return render(request, 'app1/home.html', {})

def cview(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/cust.html', {'form': form})

def sview(request):
    cust = Customer.objects.all()
    return render(request, 'app1/show.html', {'obj': cust})

def updateview(request, pk):
    obj = Customer.objects.get(cid=pk)
    form = CustomerForm(instance=obj)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/cust.html', {'form': form})

def deleteview(request, x):
    ###method-1
    '''
    obj = Customer.objects.get(cid=x)
    obj.delete()
    return redirect('/a1/sv/')
    '''

    ##method-2----->confirmation Page
    obj = Customer.objects.get(cid=x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv/')
    return render(request, 'app1/success.html', {})