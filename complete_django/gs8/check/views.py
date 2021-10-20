from django import http
# setting static and templates folders

from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return render(request,'home.html')
