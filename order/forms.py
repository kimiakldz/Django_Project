from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class': 'col form-control bg-secondary text-center',
    }))


class DiscountCodeForm(forms.Form):
    code = forms.CharField(label='', widget=forms.TextInput(attrs={

        'class': 'form-control p-4',
        'placeholder': 'Coupon Code'
    }))