from django.urls import path

from Jewelry_store.products.views import details_product, add_product, delete_product

urlpatterns = (
    path('details/<int:pk>/', details_product, name='details product'),
    path('product-add/', add_product, name='add product'),
    path('product-delete/<int:pk>/', delete_product, name='delete product'),

)