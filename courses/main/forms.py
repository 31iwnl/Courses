from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, EmailInput, PasswordInput, FileInput, FloatField, CharField
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the username'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the firstname'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Enter the email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Enter the password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Repeat the password'}))
    user_role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the role'}), initial='User')

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "password1", "password2", "user_role"]


class UpdateUserForm(UserChangeForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the username'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the firstname'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Enter the email'}))
    user_role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the role"}))

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "user_role"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Enter the password'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'link', 'price']

        widgets = {

            'product_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название курса'

            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание курса'

            }),
            'link': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на курс'

            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену курса'

            })
        }
