from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.utils import timezone
from .models import Product
from .forms import AddProductForm 
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

def product_add(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST) 
       
        if form.is_valid():
            form.save() 
            return render(request, 'products/product_add_successful.html')
    else:  
        form = AddProductForm()
    context = {
        'form':form
    }      
    return render(request, 'products/product_add_edit.html',context)

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
       form = AddProductForm(request.POST, instance=product) 
       if form.is_valid():
            form.save() 
            return render(request, 'products/product_edit_successful.html')
    else:  
        form = AddProductForm(instance=product) 
    context = {
        'form':form
    }     
    return render(request, 'products/product_add_edit.html',context) 

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
       form = AddProductForm(request.POST, instance=product) 
       if form.is_valid():
            product.delete()
            #return render(request, 'products/product_confirm_del.html')
            return HttpResponseRedirect('/')
    else:  
        form = AddProductForm(instance=product) 
    context = {
        'form':form
    }     
    return render(request, 'products/product_delete.html',context)  

def show_time(request):
    now = timezone.now() 
    return render(request, 'time.html',{'time': now}) 