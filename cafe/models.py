from django.db import models


class Order(models.Model):
    """ Модель заказа стола """

    class Status(models.TextChoices):
        """ Класс для управления статусом заказа """
        WAITING = 'WT', 'В ожидании'
        READY = 'RD', 'Готово'
        PAID = 'PD', 'Оплачено'

    table_number = models.PositiveIntegerField(verbose_name='Номер стола', help_text='Укажите номер стола')
    items = models.JSONField(default=list, verbose_name='список заказанных блюд с ценами', help_text='Укажите блюдо')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, )
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.WAITING,
                              verbose_name='Статус заказа')

    def save(self, *args, **kwargs):
        # Автоматический расчёт общей стоимости при сохранении
        if self.items:
            self.total_price = sum(item['price'] for item in self.items)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Заказ №{self.pk}, столик {self.table_number}, Статус: {self.status}'
