from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ReminderViewSet, profile_list

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profiles/', profile_list, name='profile_list'),
]
