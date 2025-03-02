from django.contrib import admin
from .models import *

class Useradmin(admin.ModelAdmin):
    list_display=['username','email','password','profile_photo']

class Categoryadmin(admin.ModelAdmin):
    list_display=['name']

class Recepiesadmin(admin.ModelAdmin):
    list_display=['name','discription','category','recipe_image']


admin.site.register(User,Useradmin)
admin.site.register(Category,Categoryadmin)
admin.site.register(Recipes,Recepiesadmin)
