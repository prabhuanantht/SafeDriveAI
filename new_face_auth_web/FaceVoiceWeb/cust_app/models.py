
# Create your models here.
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    seat_settings = models.JSONField(default=dict)  # Can store seat adjustment preferences
    music_settings = models.JSONField(default=dict)  # Can store music preferences

    def __str__(self):
        return self.name
