from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dean(request):
    return HttpResponse('<h1>Rajendra is a dean of cs department')