from django import forms
from django.contrib.auth.models import *
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name','email','address','phone','quantity']

class AddrecipeForm(forms.ModelForm):
    # category = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=forms.SelectMultiple(attrs={'size': 5}),
    #     required=True,
    #     label="Select Category(s)"
    # )
    class Meta:
        model = Recipes
        fields = ['name', 'discription', 'recipe_ingredients', 'recipe_instructions', 'recipe_image']