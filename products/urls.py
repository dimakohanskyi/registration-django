from django.contrib import admin
from django.urls import path, include
from .views import   basket, basket_add, basket_remove, ProductsListView



app_name = 'products'


urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),

    path('basket/', basket, name='basket'),
    path('basket/add/<int:product_id>/', basket_add,  name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove,  name='basket_remove')
]

