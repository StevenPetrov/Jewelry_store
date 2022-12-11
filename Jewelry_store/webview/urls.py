from django.urls import path

from Jewelry_store.webview.views import index, profile_details, UserEditView, add_product, UserDeleteView, \
    details_product, full_details_profile_owned, delete_product, store_view

urlpatterns = (
    path('', index, name='index'),
    path('profile/', profile_details, name='profile details'),
    path('profile-update/<int:pk>/', UserEditView.as_view(), name='profile edit'),
    path('product-add/', add_product, name='add product'),
    path('profile-delete/<int:pk>/', UserDeleteView.as_view(), name='profile delete'),
    path('product-details/<int:pk>/', details_product, name='details product'),
    path('profile/items', full_details_profile_owned, name='all products owned'),
    path('product-delete/<int:pk>/', delete_product, name='delete product'),
    path('store', store_view, name='store view'),
)
