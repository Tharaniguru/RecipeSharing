from django.shortcuts import render,redirect
from .models import *
import re
from django.contrib.auth import login,logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required


def Home_view(request):
    recipies=Recipes.objects.all().order_by('-id')
    return render(request,'home.html',{'recipies':recipies})

@login_required
def profile_view(request):
    user_recipes = Recipes.objects.filter(user=request.user).order_by('-id')
    user_orders=Order.objects.filter(customer=request.user)
    to_deliver=Order.objects.filter(product__user=request.user).exclude(customer=request.user)
    context = {
        'user_recipes': user_recipes,
        'user_orders': user_orders,
        'to_deliver': to_deliver,
    }
    return render(request, "profile.html",context)

# def categories_view(request):
#     categories = Category.objects.all()
#     return render(request ,"categories.html" ,{'categories':categories})


# def categorydisplay_view(request, id):
#     category = get_object_or_404(Category, id=id)
#     foods = Recipes.objects.filter(category=category)
#     return render(request, "categorydisplay.html", {"foods": foods, "category": category})

@login_required
def recipedetail_view(request,id):
    recipedetail=Recipes.objects.filter(id=id)
    print(recipedetail)
    return render(request,"displayfood.html",{'recipedetail':recipedetail})

@login_required
def addrecipe_view(request):
    if request.method == "POST":
        form = AddrecipeForm(request.POST,request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.latitude = request.POST.get('latitude')
            recipe.longitude = request.POST.get('longitude')
            recipe.user = request.user
            recipe.save()
            form.save_m2m()
            messages.success(request, "Recipe added successfully.")
            return redirect("home")  
    else:
        form = AddrecipeForm()
    return render(request, "addrecipe.html",{'form':form})


@login_required
def order_view(request, id):
    recipe = get_object_or_404(Recipes, id=id)  

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.latitude = request.POST.get('latitude')
            order.longitude = request.POST.get('longitude')
            order.product = recipe
            order.customer = request.user
            order.save()
            messages.success(request, "Order placed successfully.")
            return redirect('profile')
    else:
        form = OrderForm()

    return render(request, "order.html", {'form': form, 'recipe': recipe})




@login_required
def delete_recipe_view(request, id):
    recipe = get_object_or_404(Recipes, id=id, user=request.user)
    recipe.delete()
    messages.success(request, "Recipe deleted successfully.")
    return redirect("profile")



def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            user.set_password(raw_password)  
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
            return redirect("home")  
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def follow_view(request):
    pass


@login_required
def orderdetails_view(request,id):
    detail=get_object_or_404(Order,id=id)
    return render(request,"orderdetail.html",{"detail":detail})

