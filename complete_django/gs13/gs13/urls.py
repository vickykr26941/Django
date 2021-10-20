
from django.contrib import admin
from django.urls import path,include
from main_site import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home-page'),
    path('about/',views.about,name = 'about-page'),
    path('course/',include('course.urls'))
    
]
