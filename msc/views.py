from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def maths(request):
    return HttpResponse('<h1>mathematics is a beautiful subject</h1>')

def physics(request):
    return HttpResponse('<h1>physics</h1>')
