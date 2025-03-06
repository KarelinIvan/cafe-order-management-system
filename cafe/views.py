from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Order
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Представление для добавления нового заказа
class AddOrder(CreateView):
    model = Order
    fields = ['table_number', 'items']
    template_name = 'cafe/add_order.html'
    success_url = reverse_lazy('cafe:order_list')

    def form_valid(self, form):
        # Расчет общей стоимости заказа
        items = form.cleaned_data['items']
        total_price = sum(item['price'] for item in items)
        order = form.save(commit=False)
        order.total_price = total_price
        order.save()
        return super().form_valid(form)


# Представление для списка всех заказов
class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'cafe/order_list.html'


# Представление для удаления заказа
class DeleteOrder(DeleteView):
    model = Order
    success_url = reverse_lazy('cafe:order_list')
    template_name = 'cafe/delete_order.html'


# Представление для изменения статуса заказа
class ChangeStatus(UpdateView):
    model = Order
    fields = ['status']
    template_name = 'cafe/change_status.html'
    success_url = reverse_lazy('cafe:order_list')


# Представление для расчета выручки за смену
def calculate_revenue(request):
    paid_orders = Order.objects.filter(status='paid')
    revenue = sum(order.total_price for order in paid_orders)
    context = {'revenue': revenue}
    return render(request, 'cafe/calculate_revenue.html', context)
