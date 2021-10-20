# templates inside application 
# templates inside application and inside project as well 

from django.shortcuts import render

def learn_django(request):
    context = {
        'course_name' : 'Python Djnago',
        'student_name' : 'vicky kumar',
        'student_roll' : '18CS98'
    }
    return render(request,'course/learn_django.html',context)

def learn_python(request):
    context = {
        'course_name' : 'Python Programming',
        'student_name' : 'vicky kumar',
        'student_roll' : '18CS98'
    }
    return render(request,'course/learn_python.html')

