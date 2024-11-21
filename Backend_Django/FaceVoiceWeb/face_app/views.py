from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Profile, Reminder
from .serializers import ProfileSerializer, ReminderSerializer
from rest_framework.decorators import action


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if name:
            # Check if a profile with this name already exists
            profile = Profile.objects.filter(name=name).first()
            if profile:
                serializer = self.get_serializer(profile)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return super().create(request, *args, **kwargs)

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


from django.shortcuts import render
from .models import Profile

def profile_list(request):
    profiles = Profile.objects.all()  # Fetch all profiles
    return render(request, 'profile_list.html', {'profiles': profiles})


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # Custom action to update seat settings
    @action(detail=True, methods=['patch'])
    def update_seat_settings(self, request, pk=None):
        profile = self.get_object()
        profile.seat_settings = request.data.get('seat_settings', profile.seat_settings)
        profile.save()
        return Response({'status': 'Seat settings updated'})

    # Custom action to update music playlist
    @action(detail=True, methods=['patch'])
    def update_music_settings(self, request, pk=None):
        profile = self.get_object()
        profile.music_settings = request.data.get('music_settings', profile.music_settings)
        profile.save()
        return Response({'status': 'Music settings updated'})