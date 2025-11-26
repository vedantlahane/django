from django.shortcuts import render

# Create your views here.

from .forms import ContactForm

def user_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request,'success.html',{'data':form.cleaned_data})
        
    else:
        form = ContactForm()
    
    return render(request,'user.html',{'form':form})