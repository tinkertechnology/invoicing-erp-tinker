from django.forms import ModelForm
from django import forms
from .models import Order, Product, Table

class OrderForm(ModelForm):
    OPTIONS = (
        ('Postpay','Postpay'),
        ('Prepay (Full)','Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Ready', 'Ready'),
        ('Send', 'Send'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active='1'), empty_label='')
    table_id = forms.ModelChoiceField(queryset=Table.objects.filter(active='1'), empty_label='')
    delivery_date = forms.DateField(required=True)
    quantity = forms.IntegerField(initial=1)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','payment_option','quantity','order_status', 'table_id']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_details','price']


class TakeOrderForm(ModelForm):
    RESTURANTS = (
        ('Chinese', 'Chinese'),
        ('Japanese', 'Japanese')
    )

    order_room = forms.TypedChoiceField(required=True, choices=RESTURANTS, widget=forms.RadioSelect)


class TableForm(ModelForm):
    table_name = forms.CharField(required=True, max_length=200)
    table_number = forms.IntegerField(required=True)

    class Meta:
        model = Table
        fields = ['table_name','table_number']

class CategoryForm(ModelForm):
    category_name = form.Charfield(required=True, max_length=200)

    class Meta:
        model = Category
        fields = ['category_name']