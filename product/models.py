from django.db import models
from uuid import uuid4

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50, help_text="Name of the Product")
    size = models.PositiveIntegerField(blank=True, null=True,)
    price = models.PositiveIntegerField('AMOUNT')
    in_stock = models.PositiveIntegerField()
    cover = models.ImageField(upload_to='product/images')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def price_in_kobo(self):
        return int(str(self.price)+'00')

class ProductImages(models.Model):
    name = models.CharField(max_length=100, default=uuid4)
    img = models.ImageField(upload_to='product/images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

