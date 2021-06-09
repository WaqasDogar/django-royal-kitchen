from django import forms
from django.shortcuts import redirect, render
from .forms import *
from .models import *
# Create your views here.

def temp(request):
    offerset = Offers.objects.all()
    dataset = Customer.objects.all()
    foodset = Food.objects.all()
    return render(request,'Myapp/index.html',{'dat':dataset,'offers':offerset,'product':foodset})

def savecustomer(request):
    form = cusform()
    if request.method == 'POST':
        form = cusform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/customers')
    context ={'form':form}
    return render(request,'Myapp/Customerform.html',context)

def updatecustomer(request,pk):
    form1= Customer.objects.get(id=pk)
    form=cusform(instance=form1)
    if request.method == 'POST':
        form = cusform(request.POST,instance=form1)
        if form.is_valid:
            form.save()
           # return redirect('/customers')
    context ={'form':form1}
    return render(request,'Myapp/updatecustomer.html',context)

def deletecustomer(request,pk):
    form1= Customer.objects.get(id=pk)
    form1.delete()
    return redirect('index')