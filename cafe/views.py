from django.shortcuts import render
from .models import Order
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class AddOrder(CreateView):
    """ Для добавления нового заказа """
    model = Order
    fields = ['table_number', 'items']
    template_name = 'cafe/add_order.html'
    success_url = reverse_lazy('cafe:order_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # После успешного сохранения выводим сообщение об успешной операции
        return response


class OrderList(ListView):
    """ Отображает список всех заказов """
    model = Order
    context_object_name = 'orders'
    template_name = 'cafe/order_list.html'


class DeleteOrder(DeleteView):
    """ Для удаления заказа """
    model = Order
    success_url = reverse_lazy('cafe:order_list')
    template_name = 'cafe/delete_order.html'


class ChangeStatus(UpdateView):
    """ Для изменения статуса заказа """
    model = Order
    fields = ['status']
    template_name = 'cafe/change_status.html'
    success_url = reverse_lazy('cafe:order_list')


def calculate_revenue(request):
    """ Для расчёта общей выручки """
    paid_orders = Order.objects.filter(status='paid')
    # Проверяем наличие оплаченных заказов
    if paid_orders.exists():
        # Рассчитываем выручку как сумму total_price всех оплаченных заказов
        revenue = sum(order.total_price for order in paid_orders)
    else:
        # Если оплаченных заказов нет, устанавливаем выручку равной нулю
        revenue = 0
    context = {'revenue': revenue}
    return render(request, 'cafe/calculate_revenue.html', context)
