# resolving conflict in url pattern 

from django.shortcuts import render
from django.http import HttpResponse 

def django_course_function(request):
    return HttpResponse('hello from django course app')
