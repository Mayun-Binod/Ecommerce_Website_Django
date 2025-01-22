from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password=forms.CharField(label=_('password'),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"current-password",'class':'form-control'}))


class MypaswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_('Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autofocus':'current-password','autofocus':True,'class':'form-control'}))
    new_password1=forms.CharField(label=_('new Password'),strip=False,widget=forms.PasswordInput(attrs={'autofocus':'current-password','autofocus':True,'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_('Confirm new Password'),strip=False,widget=forms.PasswordInput(attrs={'autofocus':'current-password','autofocus':True,'class':'form-control'}))