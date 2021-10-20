# django 2nd lecture 
# multiple function based views 


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('home page')
    
def learn_django(request):
    return HttpResponse('hello django')

def learn_python(request):
    return HttpResponse('hello python')

def learn_java(request):
    return HttpResponse('hello java')

def learn_cpp(request):
    return HttpResponse('hello c++')

def learn_javascript(request):
    return HttpResponse('hello javascript')



