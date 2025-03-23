from django.shortcuts import render
from .models import Category,Recipes
import re

def Home_view(request):
    recipies=Recipes.objects.all()
    return render(request,'home.html',{'recipies':recipies})

def login_view(request):
    return render(request, "login.html")


def signup_view(request):
    return render(request, "signup.html")


def profile_view(request):
    return render(request, "profile.html")
 

def categories_view(request):
    categories = Category.objects.all()
    return render(request ,"categories.html" ,{'categories':categories})


def recipedetail_view(request,name):
    recipedetail=Recipes.objects.filter(name=name)
    print(recipedetail)
    return render(request,"displayfood.html",{'recipedetail':recipedetail})

def addrecipe_view(request):
    return render(request,"addrecipe.html")