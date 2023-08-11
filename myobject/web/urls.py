"""myobject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from web.views import index,cart,orders
urlpatterns = [

    path('', index.index,name='index'),
    path('login',index.login,name="web_login"),
    path('dologin',index.dologin,name="web_dologin"),
    path('logout',index.logout,name="web_logout"),

    path("web/",include([
        path('', index.webindex,name='web_index'),
        path('<int:Cid>', index.type,name='web_index_type'),
        #cart
        path('cart/add/<str:pid>', cart.add,name='web_cart_add'),
        path('cart/delete/<str:pid>', cart.delete,name='web_cart_delete'),
        path('cart/clear', cart.clear,name='web_cart_clear'),
        path('cart/change', cart.change,name='web_cart_change'),

        #order
        path('orders/insert',orders.insert,name='web_order_insert'),
        path('orders/<int:Oindex>',orders.index,name='web_order_index'),
        path('orders/detail',orders.detail,name='web_order_detail'),
        path('orders/status',orders.status,name='web_order_status'),
        path('orders/paymentstatus',orders.paymentstatus,name='web_order_paymentstatus'),


    ]))

]