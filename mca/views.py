from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dean(request):
    return HttpResponse('jissey is a dean of mca')
