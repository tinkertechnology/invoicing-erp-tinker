from django.forms import ModelForm
from django import forms
from .models import Order, Product, Table, Category, Customer, Bill

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
    customer_id = forms.ModelChoiceField(queryset=Customer.objects.filter(active='1'), empty_label='')
    delivery_date = forms.DateField(required=True)
    quantity = forms.IntegerField(initial=1)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','payment_option','quantity','order_status', 'table_id', 'customer_id']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        category = forms.ModelChoiceField(queryset=Category.objects.filter(active='1'), empty_label='')
        fields = ['product_name','product_details','price', 'category']


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
    category_name = forms.CharField(required=True, max_length=200)
    class Meta:
        model = Category
        fields = ['category_name']


class CustomerForm(ModelForm):
    name = forms.CharField(required=True, max_length=200)
    pan = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    
    class Meta:
        model = Customer
        fields = ['name', 'pan', 'phone', 'email', 'address']


class BillForm(ModelForm):
    Customer = forms.ModelChoiceField(queryset=Customer.objects.filter(active='1'), empty_label='')
    Table = forms.ModelChoiceField(queryset=Table.objects.filter(active='1'), empty_label='')
    date = forms.DateField(required=False)
    billno = forms.IntegerField(initial=0)
    #bill_type = models.CharField(max_length=100, null=True)
    #user_str = models.CharField(max_length=100, null=True)
    #sub_total = models.FloatField(default=0)
    discount_percent = forms.FloatField(initial=0)
    discount_amount = forms.FloatField(initial=0)
    #net_amount = models.FloatField(default=0)
    service_charge_percent = forms.FloatField(initial=0)
    #service_charge_amount = models.FloatField(default=0)
    #taxable_amount = models.FloatField(default=0)
    vat_percent = forms.FloatField(initial=0)
    pan = forms.CharField(initial=0)
    #vat_amount = models.FloatField(default=0)
    #total_amount = models.FloatField(default=0)
    #active = models.IntegerField(default=1)

    class Meta:
        model = Bill
        fields = ['Customer','Table', 'date', 'billno', 
    'discount_amount','discount_percent','service_charge_percent', 'vat_percent', 'pan']

