from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    # Save last viewed plant ID in cookie
    response = render(request, 'plant_detail.html', {'plant': plant})
    response.set_cookie('last_viewed_plant', plant_id, max_age=3600)  # 1 hour
    return response

def home(request):
    last = request.COOKIES.get('last_viewed_plant')
    if last:
        return redirect('plant_detail', plant_id=last)
    return render(request, 'home.html')

def choose_color(request):
    color = request.GET.get('color')

    response = render(request, 'choose_color.html', {
        'selected_color': request.COOKIES.get('pot_color')
    })

    if color:
        response.set_cookie('pot_color', color, max_age=86400)  # 1 day

    return response
