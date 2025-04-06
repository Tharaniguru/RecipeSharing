from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)
    category_image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

class Recipes(models.Model):
    name=models.CharField(max_length=50)
    discription=models.CharField(max_length=500,null=True,blank=True)
    recipe_ingredients=models.CharField(max_length=500,null=True,blank=True)
    recipe_instructions=models.CharField(max_length=500,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category',null=True,blank=True)
    recipe_image=models.ImageField(null=True , blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_name}"