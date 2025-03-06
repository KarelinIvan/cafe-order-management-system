from django.urls import path

from .apps import CafeConfig
from .views import AddOrder, OrderList, DeleteOrder, ChangeStatus, calculate_revenue

app_name = CafeConfig.name

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('add/', AddOrder.as_view(), name='add_order'),
    path('<int:pk>/delete/', DeleteOrder.as_view(), name='delete_order'),
    path('<int:pk>/change-status/', ChangeStatus.as_view(), name='change_status'),
    path('revenue/', calculate_revenue, name='calculate_revenue'),
]