from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    username = forms.CharField()
    security_answer = forms.CharField(widget=forms.TextInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
