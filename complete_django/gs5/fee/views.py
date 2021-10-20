

# resolving conflict in url pattern 

from django.shortcuts import render
from django.http import HttpResponse 

def django_fee_function(request):
    return HttpResponse('hello django from fee app')