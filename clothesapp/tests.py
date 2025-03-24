from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from clothesapp import models


class ColorModelTest(TestCase):

    def test_create_color(self):
        color = models.Color.objects.create(name="Red")
        self.assertEqual(models.Color.objects.count(), 1)
        self.assertEqual(color.name, "Red")


class ClothesModelTest(TestCase):
    def test_create_clothes(self):
        clothes = models.Clothes.objects.create(
            name="T-Shirt",
            color=models.Color.objects.create(name="Red"),
            price=1000,
            pic=SimpleUploadedFile("test.jpg", b"file_content"),
            backpic=SimpleUploadedFile("back_test.jpg", b"file_content")
        )
        self.assertEqual(models.Clothes.objects.count(), 1)
        self.assertEqual(clothes.name, "T-Shirt")
        self.assertEqual(clothes.color.name, "Red")
        self.assertEqual(clothes.price, 1000)
        self.assertTrue(clothes.pic)
        self.assertTrue(clothes.backpic)


class CartItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаем тестовый объект Color
        cls.color = models.Color.objects.create(name="Red")

        # Создаем тестовый объект Clothes
        cls.clothes = models.Clothes.objects.create(
            name="T-Shirt",
            color=cls.color,
            price=1000,
            pic="test.jpg",
            backpic="back_test.jpg"
        )

    def test_create_cart_item(self):
        cart_item = models.CartItem.objects.create(
            clothes=self.clothes,
            size="M"
        )
        self.assertEqual(models.CartItem.objects.count(), 1)
        self.assertEqual(cart_item.clothes.name, "T-Shirt")
        self.assertEqual(cart_item.size, "M")
