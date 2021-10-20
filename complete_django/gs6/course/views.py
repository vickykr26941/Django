# url dispatcher 
# url patterns inside each application 

from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse('hello django from course app')

def learn_python(request):
    return HttpResponse('hello python form course app')

