from django.contrib import admin
from .models import *

@admin.register(Genre)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Disc)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass