import email
from inspect import Attribute
from django.contrib.auth import authenticate
from accounts.models.ngouser import NGO_User
from django import forms

class SignInForm(forms.ModelForm):

    class Meta:
        model = NGO_User
        fields = ('email', 'password')
        widgets = {
            'email':forms.TimeField(attrs={'id': 'email', 'placeholder':'Your Name'}),
            'password' : forms.PasswordInput(attrs={'id': 'password', 'placeholder':'Your Password'}),
        }