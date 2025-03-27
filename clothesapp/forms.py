from django import forms
from clothesapp import models


class CartForm(forms.ModelForm):
    class Meta:
        model = models.CartItem
        fields = ['size']


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['email', 'address']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'address'
            })
        }
