from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('list/', OrderListView.as_view(), name='order_list'),
    path('add/', OrderCreateView.as_view(), name='order_add'),
    path('detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('update/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),
]
