from django import forms
from .models import Products
from django.forms import ModelForm

SIZE_CHOICE = [
    ('small','small'),
    ('medium','medium'),
    ('large','large')
]

class ProductForm(forms.Form):
    size = forms.ChoiceField(choices=SIZE_CHOICE,label='')
    quantity = forms.IntegerField(label='',initial=1)

class UploadModelForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name','price','description','category','image']

