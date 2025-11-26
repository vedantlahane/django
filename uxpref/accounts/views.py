from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def user_login(request):
    form = LoginForm(request.POST or None)
    message = ""
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(60*60*24*30)  # 30 days
            else:
                request.session.set_expiry(0)  # Browser close
            return redirect('preferences')
        else:
            message = "Invalid credentials"

    return render(request, 'login.html', {'form': form, 'message': message})

def user_logout(request):
    logout(request)
    return redirect('login')

def preferences(request):
    # Retrieve preferences from cookies
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'en')

    if request.method == "POST":
        theme = request.POST.get('theme', 'light')
        language = request.POST.get('language', 'en')
        response = redirect('preferences')
        response.set_cookie('theme', theme, max_age=86400*30)
        response.set_cookie('language', language, max_age=86400*30)
        return response

    return render(request, 'preferences.html', {'theme': theme, 'language': language})
