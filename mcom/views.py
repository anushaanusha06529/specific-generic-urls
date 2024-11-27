from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def function(request):
    return HttpResponse('FUNCTION PERFORM SEPCIFIC TASK')

def fun(request):
    return HttpResponse('function is a independent block')
                                
