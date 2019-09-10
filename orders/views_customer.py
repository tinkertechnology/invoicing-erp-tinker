from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Product, Table, Customer
from django.db.models import Count
from .forms import OrderForm, ProductForm, TableForm, CustomerForm
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required






#customer


@login_required
def index(request):
    # tables = Table.objects.all()
    customer = Customer.objects.filter(active='1')
    return render(request, 'Customer/index.html', {'customer': customer})    

@login_required
def new(request):
    if request.POST:
        form = CustomerForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/customer', messages.success(request, 'Cateogry was successfully created.', 'alert-success'))
            else:
                return redirect('/customer', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/customer', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = CustomerForm()
        return render(request, 'Customer/new.html', {'form':form})    


@login_required
def edit(request, id):
    customer = Customer.objects.get(id=id)
    if request.POST:
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            if form.save():
                return redirect('/customer', messages.success(request, 'customer was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = CustomerForm(instance=customer)
        return render(request, 'Customer/new.html', {'form':form})


@login_required
def destroy(request, id):
    #order = Order.objects.filter(product_id=product_id).count()

    #if order > 0:
    #     return redirect('/products', messages.success(request, 'Cannot delete product while its order exists.', 'alert-danger'))    
    #else:
    #    product = Product.objects.get(id=product_id)
    #    product.delete()
    #    return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))      

    if Customer.objects.filter(id=id).update(active='0'):
        return redirect('/customer', messages.success(request, 'customer was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/customer', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger')) 







