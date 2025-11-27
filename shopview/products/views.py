from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
    bg_color = request.COOKIES.get('bg_color', '#ffffff')
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products, 'bg_color': bg_color})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    response = render(request, 'product_detail.html', {'product': product})
    # Save last viewed product in cookie (expires in 7 days)
    response.set_cookie('last_viewed', str(product.pk), max_age=7*24*60*60)
    return response

def set_bg_color(request):
    if request.method == "POST":
        color = request.POST.get('bg_color', '#ffffff')
        response = redirect('product_list')
        response.set_cookie('bg_color', color, max_age=7*24*60*60)
        return response
    return redirect('product_list')
