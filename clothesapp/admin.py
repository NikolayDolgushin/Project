from django.contrib import admin
from clothesapp import models


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'pic', 'backpic')
