from django.shortcuts import render

# Create your views here.


def even_odd(request):
    a =  11
    if a % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    return render(request, 'app/even_odd.html', {'result': result})

