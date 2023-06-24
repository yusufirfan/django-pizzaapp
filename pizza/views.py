from django.shortcuts import render

def home(request):
    from .models import Pizza
    pizzas = Pizza.objects.all()
    context = {
        'pizzas' : pizzas
    }
    return render(request, 'home.html', context)

from django.contrib import messages
from django.urls import reverse_lazy

from .forms import (
    Order, OrderForm
)

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)


class FixView:
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

class OrderListView(FixView, ListView):
    template_name = 'pizza/order_list.html'
    context_object_name = 'orders'
    order = ['-id']

class OrderCreateView(FixView, CreateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

class OrderDetailView(FixView, DetailView):
    template_name = 'pizza/order_detail.html'
    context_object_name = 'form'

class OrderUpdateView(FixView, UpdateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

class OrderDeleteView(FixView, DeleteView)
    pass