from django import forms
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+91-\d{10}$',
    message="Phone number must be in the format +91-xxxxxxxxxx"
)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone= forms.CharField(validators=[phone_validator])