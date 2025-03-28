from django.urls import path
from .views import *

urlpatterns = [
    path('', Home_view ,name='home'),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("profile/",profile_view, name="profile"),
    path("addrecipe/", addrecipe_view, name="addrecipe"),
    path("categories/", categories_view, name="categories"),
    path("categories/<str:name>", recipedetail_view, name="recipedetail"),
]