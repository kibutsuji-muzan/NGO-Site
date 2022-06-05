from django.shortcuts import render
from django.views import View
from accounts.forms.signinform import SignInForm
class SignInView(View):

    def get(self, request):
        Form = SignInForm()
        return render(request, 'signin.html', {'form':Form})