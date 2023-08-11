
from django.contrib import admin
from django.urls import path
from myadmin.views import index
from myadmin.views import user
from myadmin.views import category
from myadmin.views import product
urlpatterns = [
    path('', index.index,name='myadmin_index'),

    path('login',index.login,name="myadmin_login"),
    path('dologin',index.dologin,name="myadmin_dologin"),
    path('logout',index.logout,name="myadmin_logout"),

    path('user/<int:pIndex>', user.index,name='myadmin_user_index'),
    path('user/add', user.add, name='myadmin_user_add'),
    path('user/insert', user.insert, name='myadmin_user_insert'),
    path('user/del/<int:uid>', user.delete, name='myadmin_user_delete'),
    path('user/edit/<int:uid>', user.edit, name='myadmin_user_edit'),
    path('user/update/<int:uid>', user.update, name='myadmin_user_update'),

    path('category/<int:pIndex>', category.index,name='myadmin_category_index'),
    path('category/add', category.add, name='myadmin_category_add'),
    path('category/insert', category.insert, name='myadmin_category_insert'),
    path('category/del/<int:cid>', category.delete, name='myadmin_category_delete'),
    path('category/edit/<int:cid>', category.edit, name='myadmin_category_edit'),
    path('category/update/<int:cid>', category.update, name='myadmin_category_update'),

    path('product/<int:pIndex>', product.index,name='myadmin_product_index'),
    path('product/add', product.add, name='myadmin_product_add'),
    path('product/insert', product.insert, name='myadmin_product_insert'),
    path('product/del/<int:pid>', product.delete, name='myadmin_product_delete'),
    path('product/edit/<int:pid>', product.edit, name='myadmin_product_edit'),
    path('product/update/<int:pid>', product.update, name='myadmin_product_update'),
]
