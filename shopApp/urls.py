from django.urls import path
from shopApp.views import *

urlpatterns = [
    path('', show_shop, name='shop'),
    path('products/<product_pk>', show_product, name='products'),
]
