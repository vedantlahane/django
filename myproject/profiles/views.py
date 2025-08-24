from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import UserProfile

# Create your views here.

# def profile(request, username):
#     return HttpResponse(f"Welcome, {username}! This is your profile page.")



# def profile(request, username):
#     return render(request, 'profile.html', {'username' : username})


def profile(request, username):
    user = get_object_or_404(UserProfile, username=username)
    return render(request, 'profile.html', {
        'username': user.username,
        'full_name': user.full_name,
        'bio': user.bio,
    })


def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_list.html', {'users': users})

def about(request):
    return render(request, 'about.html')