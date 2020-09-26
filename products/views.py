from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.utils import timezone
from .models import Product
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
            'products':products
        }
    if products.exists():
        return render(request, 'products/view_products.html', context)
    else:
        return HttpResponseNotFound(render(request, 'products/not_found.html'))

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
            'product': product
    }
    return render(request,'products/product_details.html', context)

def show_time(request):
    now = timezone.now() 
    return render(request, 'time.html',{'time': now}) 