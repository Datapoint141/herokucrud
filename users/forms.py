from django import forms
from .models import ProductsModels
class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductsModels
        fields = '__all__'