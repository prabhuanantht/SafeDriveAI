from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from cust_app.forms import ProfileForm  # You'll create this form
import requests
from .forms import ProfileForm
from django.conf import settings  # To use BASE_URL if needed

# List all profiles
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})
# Create a new profile
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form})

# Update an existing profile
def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_form.html', {'form': form})

# Delete a profile
def profile_delete(request, pk):
    # Define the API endpoint for deleting the profile
    api_url = f"http://127.0.0.1:8000/api/profiles/{pk}/"

    if request.method == 'POST':
        # Send a DELETE request to the API
        response = requests.delete(api_url)
        if response.status_code == 204:  # 204 No Content indicates successful deletion
            return redirect('profile_list')
        else:
            # Handle errors (e.g., profile not found or server error)
            return render(request, 'error.html', {'message': 'Failed to delete profile'})

    # Render confirmation page
    return render(request, 'profile_confirm_delete.html', {'pk': pk})



def profile_detail(request, pk):
    # Fetch profile data from the API
    api_url = f"http://127.0.0.1:8000/api/profiles/{pk}/"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        profile = response.json()  # Parse the JSON response
    else:
        return render(request, '404.html', {})  # Render a 404 page if not found

    # Handle form submission for updates
    if request.method == 'POST':
        # Prepare the updated data
        updated_data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'seat_settings': request.POST.get('seat_settings'),
            'music_settings': request.POST.get('music_settings'),
        }
        # Send the update request to the API
        update_response = requests.put(api_url, json=updated_data)
        if update_response.status_code == 200:
            return redirect('profile_list')  # Redirect to profile list after update

    return render(request, 'profile_detail.html', {'profile': profile})


