from django import forms

SIZE_CHOICE = [
    ('small','small'),
    ('medium','medium'),
    ('large','large')
]

class ProductForm(forms.Form):
    size = forms.ChoiceField(choices=SIZE_CHOICE,label='')
    quantity = forms.IntegerField(label='',initial=1)
