from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class Useradmin(admin.ModelAdmin):
    list_display=['username','email','password','profile_photo']

class Categoryadmin(admin.ModelAdmin):
    list_display=['name']

class Recepiesadmin(admin.ModelAdmin):
    list_display=['name','discription','recipe_image']

# admin.site.register(Category,Categoryadmin)
admin.site.register(Recipes,Recepiesadmin)
