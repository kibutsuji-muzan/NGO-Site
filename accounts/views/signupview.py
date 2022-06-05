from django.views import View
from django.shortcuts import render
from accounts.forms.signupform import SignUpForm

class SignUpView(View):

    def get(self, request):
        Form = SignUpForm()
        return render(request, 'signup.html', {'form':Form})