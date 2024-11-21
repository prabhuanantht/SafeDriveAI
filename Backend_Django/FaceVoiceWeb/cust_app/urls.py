from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),  # List all profiles
    path('create/', views.profile_create, name='profile_create'),  # Create a new profile
    path('<int:pk>/', views.profile_detail, name='profile_detail'),  # Detail/update a specific profile
    path('<int:pk>/delete/', views.profile_delete, name='profile_delete'),  # Delete a specific profile
]
