from django.contrib import admin
from django.urls import path,include
from core.views import TestView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    # path('',test_view,name = 'test-view'),
    path('',TestView.as_view(),name = 'test-view'),
    path('api/token/',obtain_auth_token,name = 'obtain-token'),

]

