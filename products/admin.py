from django.contrib import admin
from .models import Product, Specs


class SpecsAdmin(admin.ModelAdmin):
    list_display = ('engine', 'layout')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'model', 'category' )


admin.site.register(Specs, SpecsAdmin)
admin.site.register(Product, ProductAdmin)