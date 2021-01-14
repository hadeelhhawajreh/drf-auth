from django.contrib import admin
from django.urls import path, include


from .views import HealthDetailsView, HealthListView


urlpatterns = [
    path('', HealthListView.as_view(), name='health'),
    path('/<int:pk>/', HealthDetailsView.as_view(), name='health_details'),
]