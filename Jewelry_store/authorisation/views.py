from django.contrib.auth import views as auth_views, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from Jewelry_store.authorisation.forms import SignUpForm


class SignUpView(views.CreateView):
    template_name = 'auth_handling/../../templates/auth_handling/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class SignInView(auth_views.LoginView):
    template_name = 'auth_handling/../../templates/auth_handling/sign-in.html'
    redirect_authenticated_user = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('index')


class SignOutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'auth_handling/../../templates/auth_handling/sign-out.html'

    def get_success_url(self):
        return reverse_lazy('index')
