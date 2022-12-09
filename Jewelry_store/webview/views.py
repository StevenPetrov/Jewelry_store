from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()


def index(request):
    context = {
        'albums': UserModel
    }
    return render(request, 'index.html', context)