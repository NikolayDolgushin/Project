from django import forms
from clothesapp import models


class CartForm(forms.ModelForm):
    class Meta:
        model = models.CartItem
        fields = ['size']

