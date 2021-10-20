
from django.contrib import admin
from django.urls import path
from check import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.learn_django,name = 'learn-django'),

]
