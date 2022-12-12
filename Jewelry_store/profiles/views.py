from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from Jewelry_store.products.models import Product

UserModel = get_user_model()


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
    fields = ('username', 'first_name', 'last_name', 'email', 'image_field')

    def get_success_url(self):
        return reverse_lazy('profile details')


def profile_products_owned(request):
    profile = request.user
    products = Product.objects.filter(user_id=profile.id)
    context = {
        'profile': profile,
        'products': products,
    }
    return render(request, 'products/products_owner_page.html', context)


class UserDeleteView(views.DeleteView):
    template_name = 'profile/profile delete.html'
    model = UserModel
    success_url = reverse_lazy('index')