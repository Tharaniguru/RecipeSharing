from django.shortcuts import render
from .models import Category,Recipes

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