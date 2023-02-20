from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class': 'col form-control bg-secondary text-center',
    }))
