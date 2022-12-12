from django.urls import path

from Jewelry_store.webview.views import index, store_view

urlpatterns = (
    path('', index, name='index'),
    path('store', store_view, name='store view'),
)
