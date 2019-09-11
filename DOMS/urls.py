"""DOMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from orders import views as my_order
from orders import views_customer as my_customer
from orders import views_bill as my_bill
from django.contrib.auth.views import (LoginView, LogoutView, 
    PasswordChangeView, PasswordChangeDoneView, 
    PasswordResetView, PasswordResetDoneView,)
#from django.contrib.auth.views import password_change, password_change_done
#from django.contrib.auth.views import (PasswordResetView)
#from django.contrib.auth import views as auth
#from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_order.index, name='home'),
    url(r'^orders$', my_order.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
    url(r'^order/new/$', my_order.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='delete'),

    # url(r'^take_orders$', my_order.take_order_index, name='take_orders'),
    # url(r'^take_order/(?P<order_id>\d+)/$', my_order.take_order_show, name='take_order_show'),
    # url(r'^take_order/new/$', my_order.take_order_new, name='take_order_new'),
    # url(r'^take_order/edit/(?P<order_id>\d+)/$', my_order.take_order_edit, name='take_order_edit'),
    # url(r'^take_order/delete/(?P<order_id>\d+)/$', my_order.take_order_destroy, name='take_order_delete'),
    

    #TABLE 



    url(r'^table$', my_order.table_index, name='table'),
    #url(r'^take_order/(?P<order_id>\d+)/$', my_order.take_order_show, name='take_order_show'),
    url(r'^table/new/$', my_order.table_new, name='table_new'),
    url(r'^table/edit/(?P<tables_id>\d+)/$', my_order.table_edit, name='table_edit'),
    url(r'^table/delete/(?P<tables_id>\d+)/$', my_order.table_destroy, name='table_delete'),
  


    #CATEGORY 



    url(r'^category$', my_order.category_index, name='category'),
    #url(r'^take_order/(?P<order_id>\d+)/$', my_order.take_order_show, name='take_order_show'),
    url(r'^category/new/$', my_order.category_new, name='category_new'),
    url(r'^category/edit/(?P<category_id>\d+)/$', my_order.category_edit, name='category_edit'),
    url(r'^category/delete/(?P<category_id>\d+)/$', my_order.category_destroy, name='category_delete'), 


    #ORDER_UNFINISHED_
    path('table_unfinished_order/<int:table_id>/', my_order.table_unfinished_order, name= 'table_unfinished_order'),


   #CUSTOMER 

    url(r'^customer$', my_customer.index, name='customer'),
    #url(r'^take_order/(?P<order_id>\d+)/$', my_order.take_order_show, name='take_order_show'),
    url(r'^customer/new/$', my_customer.new, name='customer_new'),
    url(r'^customer/edit/(?P<id>\d+)/$', my_customer.edit, name='customer_edit'),
    url(r'^customer/delete/(?P<id>\d+)/$', my_customer.destroy, name='customer_delete'), 

    #Bill

       #CUSTOMER 

    url(r'^bill$', my_bill.index, name='bill'),
    #url(r'^take_order/(?P<order_id>\d+)/$', my_order.take_order_show, name='take_order_show'),
    url(r'^bill/new/$', my_bill.new, name='bill_new'),
    url(r'^bill/edit/(?P<id>\d+)/$', my_bill.edit, name='bill_edit'),
    url(r'^bill/delete/(?P<id>\d+)/$', my_bill.destroy, name='bill_delete'), 






    #PRODUCTS

    url(r'^products$', my_order.index_product, name='home_product'),
    url(r'^product/new/$', my_order.new_product, name='new_product'),
    url(r'^product/delete/(?P<product_id>\d+)/$', my_order.destroy_product, name='delete_product'),
    url(r'^users/login/$', LoginView.as_view(template_name ='login.html'), name='login'),
    url(r'^users/logout/$', LogoutView.as_view(next_page= '/'), name='logout'),
    #url(r'^users/change_password/$', login_required(PasswordChangeView.as_view(post_change_redirect = '/', template_name ='change_password.html')), name='change_password'),
    url(r'^users/change_password/$', login_required(PasswordChangeView.as_view(template_name ='change_password.html')), name='change_password'),
    url(r'^users/password-change/done$', login_required(PasswordChangeDoneView.as_view(template_name='password_change_done.html')), {'next': '/'} , name='password_change_done'),
    #url(r'^users/password/change/done$', login_required(PasswordResetDoneView.as_view(template_name ='change_password.html' )), name='change_password_done'),
]
