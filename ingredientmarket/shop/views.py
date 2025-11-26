from django.shortcuts import render
from .models import Ingredient, Category

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    categories = Category.objects.all()
    return render(request, 'ingredient_list.html', {
        'ingredients': ingredients,
        'categories': categories,
    })
from django.http import HttpResponse

def search_ingredients(request):
    keyword = request.GET.get('keyword', '')
    category = request.GET.get('category', '')

    items = Ingredient.objects.all()

    if keyword:
        items = items.filter(name__icontains=keyword)
    if category:
        items = items.filter(category_id=category)

    html = ""
    for item in items:
        html += f"""
        <div class='card'>
            <img src='{item.image.url}' width='120'>
            <h3>{item.name}</h3>
            <p>₹{item.price}</p>
            <button>Add to Cart</button>
        </div>
        """
    return HttpResponse(html)
