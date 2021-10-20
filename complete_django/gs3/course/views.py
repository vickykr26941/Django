# lecture 3 django 
# note : same view function can be render on different - different url 
# see urls.py for more details

from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse('hello django')

