from django import forms

from Jewelry_store.webview.models import Product


class ProductBaseFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')


class ProductCreateForm(ProductBaseFrom):
    pass


class ProductDeleteForm(ProductBaseFrom):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

