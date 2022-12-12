from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from Jewelry_store.products.forms import ProductCreateForm, ProductDeleteForm
from Jewelry_store.products.models import Product

UserModel = get_user_model()

def add_product(request):
    if request.method == 'GET':
        form = ProductCreateForm()
    else:
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'products/product-add.html', context)


def details_product(request, pk):
    product = Product.objects.filter(pk=pk).get()
    owner = UserModel.objects.filter(pk=product.user_id).get()
    context = {
        'product': product,
        'owner': owner
    }

    return render(
        request,
        'products/product-details.html',
        context,
    )


def delete_product(request, pk):
    product = Product.objects.filter(pk=pk).get()
    owner = UserModel.objects.filter(pk=product.user_id).get()
    if request.method == 'GET':
        form = ProductDeleteForm(instance=product)
    else:
        form = ProductDeleteForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'product': product,
        'owner': owner
    }
    return render(request, 'products/product_delete_form.html', context)

