from django.db import models


class Order(models.Model):
    """ Модель заказа стола """

    class Status(models.TextChoices):
        """ Класс для управления статусом заказа """

    WAITING = 'WT', 'В ожидании'
    READY = 'RD', 'Готово'
    PAID = 'PD', 'Оплачено'

    table_number = models.IntegerField(verbose_name='Номер стола', help_text='Укажите номер стола')
    items = models.JSONField(verbose_name='список заказанных блюд с ценами', help_text='Укажите блюдо')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.WAITING,
                              verbose_name='Статус заказа')

    def __str__(self):
        return f'Заказ №{self.pk}, столик {self.table_number}'
