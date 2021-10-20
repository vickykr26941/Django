"""gs2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from course import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('learn_django/',views.learn_django,name = 'learn-django'),
    path('learn_python/',views.learn_python,name = 'learn-python'),
    path('learn_java/',views.learn_python,name = 'learn-python'),
    path('learn_cpp/',views.learn_cpp,name = 'learn-c++'),
    path('learn_javascript/',views.learn_javascript,name = 'learn-javascript'),
    

]