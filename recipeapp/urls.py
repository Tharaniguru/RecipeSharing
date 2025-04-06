from django.urls import path
from .views import *

urlpatterns = [
    path('', Home_view ,name='home'),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path('logout/', logout_view, name='logout'),
    path("profile/",profile_view, name="profile"),
    path("addrecipe/", addrecipe_view, name="addrecipe"),
    path("categories/", categories_view, name="categories"),
    path("categories/<str:name>", recipedetail_view, name="recipedetail"),
    path("category/<str:category>",categorydisplay_view,name="category_display"),
    path("delete-recipe/<int:id>/", delete_recipe_view, name="delete_recipe"),
    path("follow/<str:user>",follow_view,name="follow"),
    path("order/<str:name>",order_view,name="order")
]