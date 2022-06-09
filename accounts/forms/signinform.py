from django.contrib.auth import authenticate
from accounts.models.ngouser import NGO_User
from django import forms

class SignInForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, required=True, widget=forms.EmailInput(attrs={'id':"email", 'placeholder':"Your Email"}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password', 'placeholder':'Your Password'}))


    class Meta:
        model = NGO_User
        fields = ('email', 'password')