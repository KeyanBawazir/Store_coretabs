from django.urls import path
from .views import new_order

urlpatterns = [
    path('', new_order, name='new_order'),
    
] 