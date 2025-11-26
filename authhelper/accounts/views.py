from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, ForgotPasswordForm

User = get_user_model()

def user_login(request):
    form = LoginForm(request.POST or None)
    message = ""
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            message = "Invalid credentials"
    return render(request, 'login.html', {'form': form, 'message': message})

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard.html')

def forgot_password(request):
    form = ForgotPasswordForm(request.POST or None)
    message = ""
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        security_answer = form.cleaned_data['security_answer']
        new_password = form.cleaned_data['new_password']

        try:
            user = User.objects.get(username=username)
            # Safely access security_answer in case the user model does not define it
            if getattr(user, "security_answer", None) == security_answer:
                user.set_password(new_password)
                user.save()
                message = "Password updated successfully!"
            else:
                message = "Incorrect security answer."
        except User.DoesNotExist:
            message = "User not found."
    return render(request, 'forgot_password.html', {'form': form, 'message': message})
