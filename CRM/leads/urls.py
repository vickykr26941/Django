
from leads.views import (
    lead_create, lead_detail,lead_delete,lead_list,lead_update,
    LeadCreateVeiw,LeadDetailView,LeadListView,LeadUpdateView,LeadDeleteView
)
from django.contrib import admin
from django.urls import path


app_name = 'leads'
urlpatterns = [
    path('',LeadListView.as_view(),name="lead-list"),
    path('<int:pk>/',LeadDetailView.as_view(),name = "lead-detail"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="lead-update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name="lead-delete"),
    path('create/',LeadCreateVeiw.as_view(),name='lead-create'),


]

