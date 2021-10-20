
from django.contrib import admin
from django.urls import path,include 
from course import views as course_views 
from fees import views as fees_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/',include([
        path('learn_django/',course_views.learn_django,name = 'learn-django-course'),
        path('learn_python/',course_views.learn_python,name = 'learn-python-course'),
    ])),
    path('fees/',include([
        path('learn_django/',fees_views.learn_django,name = 'learn-django-fees'),
        path('learn_python/',fees_views.learn_python,name = 'learn-python-fees'),
    ]))
]
