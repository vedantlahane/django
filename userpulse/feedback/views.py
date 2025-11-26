from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required

@login_required
def submit_feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('thank_you')
    return render(request, 'feedback_form.html', {'form': form})

@login_required
def thank_you(request):
    return render(request, 'thank_you.html')
