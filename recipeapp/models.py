from django.db import models

class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    profile_photo=models.ImageField(null=True,blank=True)

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
