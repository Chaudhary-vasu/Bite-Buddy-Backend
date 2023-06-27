from django.contrib import admin
from .models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','street','postalCode','city']
admin.site.register(Customer,CustomerAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user','ordered_meals','quantity']
admin.site.register(Orders,OrdersAdmin)


class MealsItemsAdmin(admin.ModelAdmin):
    list_display = ['name','description','price']
admin.site.register(MealsItems,MealsItemsAdmin)