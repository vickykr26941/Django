# django templates with dynamic data's 
# seperate template folder for each application 
# django filters // filters in django templates
# jinja if else and operators and conditional and loops 


from django.shortcuts import render

def learn_django(request):
    context = {
        'dict_val' : {
        'course_name' : 'Python Django',
        'student_name' : 'vicky kumar',
        'student_roll' : '18CS98',
        },
        'course_name' : 'Python Django',
        'student_name' : 'vicky kumar',
        'student_roll' : '18CS98',
    }
    return render(request,'course/learn_django.html',context)

def learn_python(request):
    context = {
        'course_name' : 'Python Programming',
        'student_name' : 'vicky kumar',
        'student_roll' : '18CS98',
    }
    return render(request,'course/learn_python.html',context)


