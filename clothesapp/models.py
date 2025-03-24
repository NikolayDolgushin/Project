from django.db import models


class Color(models.Model):
    name = models.CharField(
        verbose_name="COLOR",
        max_length=255,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

    class Metha:
        verbose_name = "COLOR"
        verbose_name_plural = "COLORS"


class Clothes(models.Model):

    name = models.CharField(
        verbose_name="ITEM",
        max_length=255,
        null=False,
        blank=False
    )
    color = models.ForeignKey(Color, verbose_name="COLOR", on_delete=models.CASCADE)
    price = models.IntegerField('PRICE', null=False, blank=False)
    pic = models.ImageField('PICTURE', upload_to='pics/')
    backpic = models.ImageField('BACK PICTURE', upload_to='backpics/')

    def __str__(self):
        return f'{self.color.name} {self.name}'

    def save(self, *args, **kwargs):
        if self.price < 0:
            pass
        super().save()

    class Meta:
        verbose_name = "CLOTHING"
        verbose_name_plural = "CLOTHES"


class Order(models.Model):
    STATUS_CHOICES = [
        ('processing', 'PROCESSING'),
        ('shipped', 'SHIPPED'),
        ('delivered', 'DELIVERED'),
        ('picked_up', 'PUCKED UP'),
    ]

    email = models.EmailField(verbose_name="EMAIL")
    address = models.CharField(verbose_name="АDDRESS", max_length=255)
    items = models.TextField(verbose_name="ITEMS")
    status = models.CharField(
        verbose_name="STATUS",
        max_length=20,
        choices=STATUS_CHOICES,
        default='processing',
    )
    created_at = models.DateTimeField(verbose_name="CREATION TIME", auto_now_add=True)

    def __str__(self):
        return f"ORDER #{self.id} DATED {self.created_at}"

    def set_status(self, new_status):
        if new_status in dict(self.STATUS_CHOICES).keys():
            self.status = new_status
            self.save()
        else:
            raise ValueError(f"INVALID STATUS: {new_status}")

    class Meta:
        verbose_name = "ORDER"
        verbose_name_plural = "ORDERS"


class CartItem(models.Model):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]
    clothes = models.ForeignKey(Clothes, verbose_name="CLOTHES", on_delete=models.CASCADE)
    size = models.CharField(verbose_name="SIZE", max_length=4, choices=SIZE_CHOICES)

    def __str__(self):
        return f"{self.clothes.name}"

    class Meta:
        verbose_name = "CART ITEM"
        verbose_name_plural = "CART ITEMS"
