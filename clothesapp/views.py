from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from clothesapp import models, forms


class Main(ListView):
    model = models.Clothes
    template_name = 'main.html'
    context_object_name = 'items'


class ClothesView(DetailView):
    model = models.Clothes
    template_name = 'clothes.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = forms.CartForm()  # Добавляем форму в контекст
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = forms.CartForm(request.POST)

        if form.is_valid():
            cart = form.save(commit=False)
            cart.clothes = self.object  # Связываем заказ с текущим товаром
            cart.save()
            messages.success(request, 'Товар успешно добавлен в корзину!')
            return redirect(f'/clothes/{self.object.pk}')


class Cart(ListView):
    template_name = 'cart.html'
    context_object_name = 'items'
    def get_queryset(self):
        queryset = models.CartItem.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = sum(item.clothes.price for item in self.get_queryset())
        context['total_price'] = total_price
        return context
