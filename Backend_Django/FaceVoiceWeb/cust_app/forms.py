from django import forms
from face_app.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'seat_settings', 'music_settings']
