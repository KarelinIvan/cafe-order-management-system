from django.contrib import admin

from cafe.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'items', 'total_price', 'status')
    list_filter = ('table_number', 'status',)
