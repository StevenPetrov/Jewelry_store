from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from Jewelry_store.webview.forms import ProductCreateForm, ProductDeleteForm
from Jewelry_store.webview.models import Product

UserModel = get_user_model()


def index(request):
    product = Product.objects.all()
    context = {
        'users': UserModel,
        'products': product,
    }
    return render(request, 'index.html', context)


def profile_details(request):
    profile = request.user
    products = Product.objects.filter(user_id=profile.id)
    context = {
        'profile': profile,
        'products': products,
    }
    return render(request, 'profile/profile-details.html', context)


class UserEditView(views.UpdateView):
    template_name = 'profile/profile-update.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email')

    def get_success_url(self):
        return reverse_lazy('profile details')


class UserDeleteView(views.DeleteView):
    template_name = 'profile/profile delete.html'
    model = UserModel
    success_url = reverse_lazy('index')


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


def full_details_profile_owned(request):
    profile = request.user
    products = Product.objects.filter(user_id=profile.id)
    context = {
        'profile': profile,
        'products': products,
    }
    return render(request, 'products/products_owner_page.html', context)


def store_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store.html', context)
