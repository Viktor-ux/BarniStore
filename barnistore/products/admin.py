from django.contrib import admin

from products.models import Products, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_editable = ['category']


admin.site.register(Products, ProductAdmin)
admin.site.register(Category)
