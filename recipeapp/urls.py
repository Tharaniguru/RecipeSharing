from django.urls import path
from .views import *

urlpatterns = [
    path('', Home_view ,name='home'),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path('logout/', logout_view, name='logout'),
    path("profile/",profile_view, name="profile"),
    path("addrecipe/", addrecipe_view, name="addrecipe"),
    # path("categories/", categories_view, name="categories"),
    path("recipe/<int:id>", recipedetail_view, name="recipedetail"),
    # path("category/<int:id>",categorydisplay_view,name="category_display"),
    path("delete-recipe/<int:id>/", delete_recipe_view, name="delete_recipe"),
    path("follow/<str:user>",follow_view,name="follow"),
    path("order/<int:id>",order_view,name="order"),
    path("orderdetails/<int:id>",orderdetails_view,name="order_details")
]