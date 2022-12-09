from django.urls import path

from Jewelry_store.webview.views import index

urlpatterns = (
    path('', index, name='index'),
)
