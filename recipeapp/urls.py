from django.urls import path
from .views import *

urlpatterns = [
    path('home/',Home_view,name='home')
]