
from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/',include('course.urls')),
    path('fees/',include('fees.urls')),
    path('',views.home,name = 'home-page'),
    


]
