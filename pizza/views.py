from django.shortcuts import render

def home(request):
    from .models import Pizza
    pizzas = Pizza.objects.all()
    context = {
        'pizzas' : pizzas
    }
    return render(request, 'home.html', context)