from django.urls import path
from .views import *

urlpatterns = [
    path('', Home_view ,name='home'),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("profile/",profile_view, name="profile"),
    path("categories/", categories_view, name="categories"),
]