from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Order, Recipes


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'email', 'address', 'phone', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Delivery address',
                'rows': 3
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quantity'
            }),
        }


class AddrecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'discription', 'recipe_ingredients', 'recipe_instructions', 'recipe_image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter recipe name'
            }),
            'discription': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Short description',
                'rows': 3
            }),
            'recipe_ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'List ingredients here',
                'rows': 5
            }),
            'recipe_instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Step-by-step instructions',
                'rows': 7
            }),
            'recipe_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }
