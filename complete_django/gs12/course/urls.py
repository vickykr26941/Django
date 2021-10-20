
from django.urls import path
from . import views 
urlpatterns = [
    path('learn_django/',views.learn_django,name = 'learn-django'),
    path('learn_python/',views.learn_python,name = 'learn-python'),
    
]
