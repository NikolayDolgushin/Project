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
