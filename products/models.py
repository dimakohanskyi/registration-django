from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, User


class ProductCategory(models.Model):

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return  self.name




class Product(models.Model):

    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


    def __str__(self):
        return (f"Product: {self.name} | Category: {self.category.name},"
                f" Price: {self.price}, Description: {self.description}")



class Basket(models.Model):

    user = models.ForeignKey( to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Basket for {self.user} | Product: {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)


    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)











