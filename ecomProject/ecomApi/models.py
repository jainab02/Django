from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.IntegerField(default=0,
                                 validators=[MaxValueValidator(5), MinValueValidator(0),])
    desc = models.TextField()
    cid = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}-{self.price}" 


class Cart(models.Model):
    oid = models.AutoField(primary_key=True)
    # username = models.ForeignKey
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)  # foreign key
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    # totalAmt = models.CharField(max_length=10)
    address = models.TextField()

    def calculate_total_amount(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.product.name} - {self.calculate_total_amount()} "


class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    full_name = models.CharField(max_length=50)
    orders = models.ManyToManyField(Cart)

    def __str__(self):
        return self.full_name
