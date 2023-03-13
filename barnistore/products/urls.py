from django.urls import path

from products.views import index, product, category, create

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('product/<slug:slug>/', product, name='product'),
    path('category/<slug:slug>/', category, name='category'),
    path('create/', create, name='product_create'),
]
