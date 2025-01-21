from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password1': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }
