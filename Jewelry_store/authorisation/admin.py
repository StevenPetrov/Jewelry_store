from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = SignUpForm
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_active', 'first_name', 'last_name', 'email',)
    list_filter = ('username', 'is_staff', 'is_active', 'first_name', 'last_name', 'email',)
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
