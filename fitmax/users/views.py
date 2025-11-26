from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def user_login(request):
    form = LoginForm(request.POST or None)
    message = ""
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if remember_me:
                    # Set session to expire in 30 days
                    request.session.set_expiry(60 * 60 * 24 * 30)
                else:
                    # Session expires on browser close
                    request.session.set_expiry(0)
                return redirect('dashboard')
            else:
                message = "Invalid credentials"
    return render(request, 'login.html', {'form': form, 'message': message})

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    # Example user preference
    workout_pref = request.COOKIES.get('workout_pref', 'Medium')
    return render(request, 'dashboard.html', {'workout_pref': workout_pref})

def set_preference(request):
    if request.method == "POST":
        workout_pref = request.POST.get('workout_pref', 'Medium')
        response = redirect('dashboard')
        response.set_cookie('workout_pref', workout_pref, max_age=86400*30)  # 30 days
        return response
    return redirect('dashboard')
