from django.urls import path

from Jewelry_store.profiles.views import UserEditView, UserDeleteView, profile_details, profile_products_owned

urlpatterns =(
    path('', profile_details, name='profile details'),
    path('update/<int:pk>/', UserEditView.as_view(), name='profile edit'),
    path('items', profile_products_owned, name='all products owned'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='profile delete'),


)