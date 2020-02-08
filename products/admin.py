from django.contrib import admin
from .models import Category, product, ProductBooked, UserNotes, Order, Contact, Reviews


class OrderProduct(admin.ModelAdmin):
    list_display = [
        'user',
        'items',
        'quantity',
        'date',
        'payment'
    ]


admin.site.register(Category)
admin.site.register(product)
admin.site.register(ProductBooked, OrderProduct)
admin.site.register(UserNotes)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Reviews)
