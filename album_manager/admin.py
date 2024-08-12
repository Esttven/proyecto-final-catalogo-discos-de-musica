from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelCategory):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelClient):
    pass

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelPurchase):
    pass