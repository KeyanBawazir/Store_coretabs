from django.urls import path
from .views import product_list, product_details
urlpatterns = [
    path('products/', product_list, name='view_products'),
    path('products/<pk>/', product_details,name='product_details'),
]  