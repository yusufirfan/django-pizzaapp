from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pizza


@login_required(login_url='user_login')
def home(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas' : pizzas
    }
    return render(request, 'home.html', context)

from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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


class FixView(LoginRequiredMixin):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_list')
    login_url = 'user_login'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-id')
    

class OrderListView(FixView, ListView):
    template_name = 'pizza/order_list.html'
    context_object_name = 'orders'
    # ordering = ['-id']

class OrderCreateView(FixView, CreateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        pizza_id = self.request.GET.get('pizza', 0)
        kwargs['pizza'] = Pizza.objects.filter(id=pizza_id).first()
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.pizza_id = self.request.GET.get('pizza')
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Added.')
        return super().post(request, *args, **kwargs)

class OrderDetailView(FixView, DetailView):
    template_name = 'pizza/order_detail.html'
    context_object_name = 'order'

class OrderUpdateView(FixView, UpdateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Updated.')
        return super().post(request, *args, **kwargs)

class OrderDeleteView(FixView, DeleteView):
    
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Deleted.')
        return super().delete(request, *args, **kwargs)