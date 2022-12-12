from django.contrib.auth import get_user_model
from django.shortcuts import render
from Jewelry_store.products.models import Product

UserModel = get_user_model()


def index(request):
    product = Product.objects.all()
    context = {
        'users': UserModel,
        'products': product,
    }
    return render(request, 'index.html', context)


def store_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store.html', context)
