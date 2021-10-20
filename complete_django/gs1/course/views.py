# first lecture of django 
# function based views and urls patterns in django 


from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse('Hello world')

