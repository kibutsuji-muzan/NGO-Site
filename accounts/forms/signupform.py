from django import forms
from accounts.models.ngouser import NGO_User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    CHOICES = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER'),]

    email = forms.EmailField(max_length=60, required=True, widget=forms.EmailInput(attrs={'id':"email", 'placeholder':"Your Email"}))
    phone = forms.CharField(max_length=12, required=True, widget=forms.TextInput(attrs={'id':"phonenumber", 'placeholder':"Phone Number"}))
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'id':"name", 'placeholder':"Your Name"}))
    birthday = forms.DateField(label="birthday", required=True, widget=forms.DateInput(attrs={'id':"birthday", 'placeholder':"Birthday", 'type':'date'}))
    gender = forms.CharField(required=True, widget=forms.RadioSelect(choices=CHOICES, attrs={'id':"option-1"}))

    class Meta:
        model = NGO_User
        fields = ("email", "name","phone", "birthday", "gender") 

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.name = self.cleaned_data["name"]
        user.phone = self.cleaned_data["phone"]
        user.birthday = self.cleaned_data["birthday"]
        user.gender = self.cleaned_data["gender"]

        if commit:
            user.save()
        return user