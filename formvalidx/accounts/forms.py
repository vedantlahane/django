from django import forms
from django.core.validators import RegexValidator

code_validator = RegexValidator(
    regex=r'^[A-Z]{3}[0-9]{3}$',
    message='Code must be 3 uppercase letters followed by 3 digits (e.g., ABC123)'
)

class CodeForm(forms.Form):
    code = forms.CharField(
        max_length=6,
        validators=[code_validator],
        label="Enter Code"
    )
