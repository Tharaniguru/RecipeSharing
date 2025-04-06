from django.shortcuts import render,redirect
from .models import Category,Recipes
import re
from django.contrib.auth import login,logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required


def Home_view(request):
    recipies=Recipes.objects.all().order_by('-id')
    return render(request,'home.html',{'recipies':recipies})

@login_required
def profile_view(request):
    user_recipes = Recipes.objects.filter(user=request.user).order_by('-id')
    return render(request, "profile.html",{"user_recipes": user_recipes})

def categories_view(request):
    categories = Category.objects.all()
    return render(request ,"categories.html" ,{'categories':categories})

@login_required
def recipedetail_view(request,name):
    recipedetail=Recipes.objects.filter(name=name)
    print(recipedetail)
    return render(request,"displayfood.html",{'recipedetail':recipedetail})

@login_required
def addrecipe_view(request):
    if request.method == "POST":
        name = request.POST.get("recipename")
        description = request.POST.get("recipedescription")
        ingredients = request.POST.get("recipeingrediants")
        instructions = request.POST.get("recipe")
        image = request.FILES.get("recipeimage")
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        recipe = Recipes(
            name=name,
            discription=description,
            recipe_ingredients=ingredients,
            recipe_instructions=instructions,
            recipe_image=image,
            user=request.user,
            latitude=latitude if latitude else None,
            longitude=longitude if longitude else None  
        )
        recipe.save()
        messages.success(request, "Recipe added successfully.")
        return redirect("home")  
    return render(request, "addrecipe.html")

@login_required
def delete_recipe_view(request, id):
    recipe = get_object_or_404(Recipes, id=id, user=request.user)
    recipe.delete()
    messages.success(request, "Recipe deleted successfully.")
    return redirect("profile")


def categorydisplay_view(request,category):
    foods=Recipes.objects.filter(category=category)
    return render(request,"categorydisplay.html",{"foods":foods})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            user.set_password(raw_password)  # Hash the password
            user.save()
            login(request, user)  
            return redirect("home")  
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect after login
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def follow_view(request):
    pass