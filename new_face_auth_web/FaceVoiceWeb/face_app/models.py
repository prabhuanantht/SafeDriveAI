# from django.db import models
# from django.contrib import admin

# # Define your models here
# class Profile(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True, null=True, blank=True)
#     seat_settings = models.JSONField(default=dict)
#     music_settings = models.JSONField(default=dict)

#     def __str__(self):
#         return self.name


# class Reminder(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reminders')
#     title = models.CharField(max_length=200)
#     datetime = models.DateTimeField()

#     def __str__(self):
#         return f"{self.title} - {self.profile.name}"


# # Register your models with the admin
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email')


# @admin.register(Reminder)
# class ReminderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'datetime', 'profile')


from django.db import models
from django.contrib import admin

# Profile Model
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    seat_settings = models.JSONField(default=dict)  # Example: {'height': 10, 'recline': 5}
    music_settings = models.JSONField(default=list)  # List of songs

    def __str__(self):
        return self.name



# Reminder Model
class Reminder(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reminders')
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.profile.name}"


#Customize the Admin Panel for Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'seat_settings_preview', 'music_settings_preview')
    search_fields = ('name', 'email')
    list_filter = ('email',)
    ordering = ('name',)

    # Custom method to display a summary of seat_settings
    def seat_settings_preview(self, obj):
        return f"{obj.seat_settings}"[:50]  # Truncate to 50 characters
    seat_settings_preview.short_description = 'Seat Settings'

    # Custom method to display a summary of music_settings
    def music_settings_preview(self, obj):
        return f"{obj.music_settings}"[:50]  # Truncate to 50 characters
    music_settings_preview.short_description = 'Music Settings'




# from django import forms
# from django_json_widget.widgets import JSONEditorWidget

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.JSONField: {'widget': JSONEditorWidget},
#     }
#     list_display = ('id', 'name', 'email', 'seat_settings_preview', 'music_settings_preview')



#Customize the Admin Panel for Reminder
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'datetime', 'profile')
    search_fields = ('title',)
    list_filter = ('datetime',)
    ordering = ('datetime',)


