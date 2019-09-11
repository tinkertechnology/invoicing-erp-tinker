from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Product, Table, Bill
from django.db.models import Count
from .forms import OrderForm, ProductForm, TableForm, BillForm
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required






#Bill


@login_required
def index(request):
    # tables = Table.objects.all()
    Bill = Bill.objects.filter(active='1')
    return render(request, 'Bill/index.html', {'Bill': Bill})    

@login_required
def new(request):
    if request.POST:
        form = BillForm(request.POST)
        print(form)
        if form.is_valid() or True:
            if form.save():
                return redirect('/customer', messages.success(request, 'Bill was successfully created.', 'alert-success'))
            else:
                return redirect('/customer', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/customer', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = BillForm()
        return render(request, 'Bill/new.html', {'form':form})    


@login_required
def edit(request, id):
    Bill = Bill.objects.get(id=id)
    if request.POST:
        form = BillForm(request.POST, instance=Bill)
        if form.is_valid():
            if form.save():
                return redirect('/bill', messages.success(request, 'Bill was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = BillForm(instance=Bill)
        return render(request, 'Bill/new.html', {'form':form})


@login_required
def destroy(request, id):
    #order = Order.objects.filter(product_id=product_id).count()

    #if order > 0:
    #     return redirect('/products', messages.success(request, 'Cannot delete product while its order exists.', 'alert-danger'))    
    #else:
    #    product = Product.objects.get(id=product_id)
    #    product.delete()
    #    return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))      

    if Bill.objects.filter(id=id).update(active='0'):
        return redirect('/bill', messages.success(request, 'Bill was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/bill', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger')) 







