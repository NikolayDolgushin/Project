from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from clothesapp import models, forms


class Main(ListView):
    model = models.Clothes
    template_name = 'main.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = models.Clothes.objects.all()
        color_filter = self.request.GET.get('color')
        if color_filter:
            queryset = queryset.filter(color__name=color_filter)
        sort = self.request.GET.get('sort')
        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_colors'] = models.Color.objects.all()
        context['current_color'] = self.request.GET.get('color', '')
        context['current_sort'] = self.request.GET.get('sort', '')
        return context


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
            cart.clothes = self.object
            cart.save()
            messages.success(request, 'THE ITEM HAS BEEN ADDED TO THE CART!')
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

    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')
        if item_id:
            try:
                item = models.CartItem.objects.get(id=item_id)
                item.delete()
                messages.success(request, 'ITEM HAS BEEN DELETED FROM THE CART')
            except models.CartItem.DoesNotExist:
                pass
        return redirect('/cart')
