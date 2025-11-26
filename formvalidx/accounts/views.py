from django.shortcuts import render
from .forms import CodeForm

def validate_code(request):
    form = CodeForm()
    message = ""

    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            message = "Code is valid!"
        else:
            message = "Invalid code format."

    return render(request, "validate.html", {"form": form, "message": message})
