from django.contrib import admin
from clothesapp import models


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'pic', 'backpic')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('items', 'email', 'address', 'created_at', 'status')
    list_editable = ('status', )
    list_filter = ('created_at', )


@admin.register(models.CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ('get_clothes_name', 'get_clothes_color', 'size', 'get_clothes_price')

    def get_clothes_name(self, obj):
        return obj.clothes.name
    get_clothes_name.short_description = 'NAME'

    def get_clothes_color(self, obj):
        return obj.clothes.color
    get_clothes_color.short_description = 'COLOR'

    def get_clothes_price(self, obj):
        return obj.clothes.price
    get_clothes_price.short_description = 'PRISE'
