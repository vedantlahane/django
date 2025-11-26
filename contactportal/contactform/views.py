from django.shortcuts import render
from .forms import ContactForm
# Create your views here.]

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number= form.cleaned_data['phone']
            return render(request,'success.html',{'name':name,"phone":number})
    
    else:
        form = ContactForm()
    

    return render(request,'contact.html',{'form':form})





