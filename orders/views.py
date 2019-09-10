from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Product, Table, Category
from django.db.models import Count
from .forms import OrderForm, ProductForm, TableForm, CategoryForm
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tableSelect = OrderForm()
    orders = Order.objects.order_by('table_id')
    table_id = request.GET.get('table_id')
    if table_id:
        orders = orders.filter(table_id=table_id)
    orders = orders.all()
    
    return render(request, 'index.html', {'orders': orders, 'tableSelect': tableSelect})

@login_required
def show(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'show.html', {'order': order})

@login_required
def new(request):
    if not request.user.is_staff:
        raise Http404
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
        return render(request, 'save.html', {'form':form , 'tables': tables})

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
        return render(request, 'save.html', {'form':form})

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
    return render(request, 'Category/index_category.html', {'category': category})    

@login_required
def category_new(request):
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/category', messages.success(request, 'Cateogry was successfully created.', 'alert-success'))
            else:
                return redirect('/category', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/category', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        category_form = CategoryForm()
        return render(request, 'Category/new_category.html', {'category_form':category_form})    


@login_required
def category_edit(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.POST:
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            if form.save():
                return redirect('/category', messages.success(request, 'Category was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        category_form = CategoryForm(instance=category)
        return render(request, 'Category/edit_category.html', {'category_form':category_form})


@login_required
def category_destroy(request, category_id):
    #order = Order.objects.filter(product_id=product_id).count()

    #if order > 0:
    #     return redirect('/products', messages.success(request, 'Cannot delete product while its order exists.', 'alert-danger'))    
    #else:
    #    product = Product.objects.get(id=product_id)
    #    product.delete()
    #    return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))      

    if Category.objects.filter(id=category_id).update(active='0'):
        return redirect('/category', messages.success(request, 'Category was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/category', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger')) 



@login_required
def table_unfinished_order(request, table_id):

     orders = Order.objects.filter(table_id=table_id).all()
     return render(request, 'table_unfinished_order.html', {'orders':orders})




