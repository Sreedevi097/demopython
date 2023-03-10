from django.http import HttpResponse
from django.shortcuts import render

from .models import location
from .models import location1
from django.shortcuts import render

# from . models import details
# from . models import details2
# Create your views here.

def demo(request):
    obj=location.objects.all()
    obj1 = location1.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     addition=x+y
#     subtraction=x-y
#     multiply=x*y
#     divide=x/y
#     return render(request,"result.html",{'addition':addition,'subtraction':subtraction,'multiply':multiply,'divide':divide})