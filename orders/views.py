from django.shortcuts import render, redirect
from .models import Order, Product, Table, Category
from .forms import OrderForm, ProductForm, TableForm, CategoryForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {'orders': orders})

@login_required
def show(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'show.html', {'order': order})

@login_required
def new(request):
    tables = Table.objects.all()
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form':form , 'tables': tables})

@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form':form})

@login_required
def destroy(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/', messages.success(request, 'Order was successfully deleted.', 'alert-success'))



#Product

@login_required
def index_product(request):
    products = Product.objects.filter(active='1')
    return render(request, 'index_product.html', {'products': products})    

@login_required
def new_product(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/products', messages.success(request, 'Product was successfully created.', 'alert-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        product_form = ProductForm()
        return render(request, 'new_product.html', {'product_form':product_form})    

@login_required
def destroy_product(request, product_id):
    #order = Order.objects.filter(product_id=product_id).count()

    #if order > 0:
    #     return redirect('/products', messages.success(request, 'Cannot delete product while its order exists.', 'alert-danger'))    
    #else:
    #    product = Product.objects.get(id=product_id)
    #    product.delete()
    #    return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))      

    if Product.objects.filter(id=product_id).update(active='0'):
        return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/products', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger')) 

#TABLE

@login_required
def table_index(request):
    # tables = Table.objects.all()
    tables = Table.objects.filter(active='1')
    return render(request, 'index_table.html', {'tables': tables})    

@login_required
def table_new(request):
    if request.POST:
        form = TableForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/table', messages.success(request, 'table was successfully created.', 'alert-success'))
            else:
                return redirect('/table', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/table', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        table_form = TableForm()
        return render(request, 'new_table.html', {'table_form':table_form})    


@login_required
def table_edit(request, tables_id):
    tables = Table.objects.get(id=tables_id)
    if request.POST:
        form = TableForm(request.POST, instance=tables)
        if form.is_valid():
            if form.save():
                return redirect('/table', messages.success(request, 'Table was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = TableForm(instance=tables)
        return render(request, 'edit_table.html', {'form':form})


@login_required
def table_destroy(request, tables_id):
    #order = Order.objects.filter(product_id=product_id).count()

    #if order > 0:
    #     return redirect('/products', messages.success(request, 'Cannot delete product while its order exists.', 'alert-danger'))    
    #else:
    #    product = Product.objects.get(id=product_id)
    #    product.delete()
    #    return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))      

    if Table.objects.filter(id=tables_id).update(active='0'):
        return redirect('/table', messages.success(request, 'Table was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/table', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger')) 






#CATEGORY


@login_required
def category_index(request):
    # tables = Table.objects.all()
    category = Category.objects.filter(active='1')
    return render(request, '/Category/index_category.html', {'category': category})    

@login_required
def category_new(request):
    if request.POST:
        form = TableForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/table', messages.success(request, 'table was successfully created.', 'alert-success'))
            else:
                return redirect('/table', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/table', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        table_form = TableForm()
        return render(request, 'new_table.html', {'table_form':table_form})    


@login_required
def category_edit(request, category_id):
    tables = Table.objects.get(id=category_id)
    if request.POST:
        form = TableForm(request.POST, instance=tables)
        if form.is_valid():
            if form.save():
                return redirect('/table', messages.success(request, 'Table was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = TableForm(instance=tables)
        return render(request, 'edit_table.html', {'form':form})


@login_required
def category_destroy(request, category_id):
    #order = Order.objects.filter(product_id=product_id).count()

    #if order > 0:
    #     return redirect('/products', messages.success(request, 'Cannot delete product while its order exists.', 'alert-danger'))    
    #else:
    #    product = Product.objects.get(id=product_id)
    #    product.delete()
    #    return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))      

    if Table.objects.filter(id=tables_id).update(active='0'):
        return redirect('/table', messages.success(request, 'Table was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/table', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger')) 


