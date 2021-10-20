
from django.contrib import admin
from django.urls import path,include
from course import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj',views.learn_django,name = 'learn-django'),

]
