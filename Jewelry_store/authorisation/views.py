from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views



class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class SignUpView(views.CreateView):
    template_name = 'auth_handling/sign-up.html'
    form_class = SignUpForm
    #
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'auth_handling/sign-in.html'
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    template_name = 'auth_handling/sign-out.html'


