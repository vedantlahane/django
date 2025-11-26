from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import ContactForm,CustomUserCreationForm
from .models import ContactMessage

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("<h1>Hello World</h1>")


def greet(request,user_name):
    

    task_list= [
        {'id':1,'name':'Setup Project','done':True},
        {'id':2,'name':'Map Dynamic Url','done':True},
        {'id':3,'name':'Implement Template Inheritance','done':False},
        {'id':4,'name':'Setup Form in Django','done':False},
    ]
    context = {
        'name':user_name,
        'is_admin':user_name.lower() == 'vedant',
        'project_tasks':task_list,
    }
    return render(request,'main_app/greeting.html',context)

def contact_view(request):

    count = request.session.get('visit_count',0)
    request.session['visit_count'] = count + 1


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            ContactMessage.objects.create(
                name = form.cleaned_data['name'],
                message = form.cleaned_data['message']
            )
            # print(f"Form Submitted")
            # print(f"Name: {form.cleaned_data['name']}")
            # print(f"Message: {form.cleaned_data['message']}")
            # print(f"-----------------------------")

            return redirect('contact')
        
    else:


        form = ContactForm()

    context = {'form': form,'visit_count':count + 1}

    return render(request,'main_app/contact.html',context)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            return redirect('login')
        
    else:
        form = CustomUserCreationForm()

    context= {'form':form}

    return render(request,'registration/registration.html',context)