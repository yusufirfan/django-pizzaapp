from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = [
            'user',
            'pizza',
        ]
        widgets = {
            'size': forms.RadioSelect,
        }