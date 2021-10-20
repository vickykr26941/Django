from django.urls import path,include
from . import views

urlpatterns = [
   path('learn_django/',views.learn_django,name = 'fees-learn-django'),
   path('learn_python/',views.learn_python,name = 'fees-learn-python'),

]
