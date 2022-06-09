from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from accounts.forms.signinform import SignInForm

class SignInView(View):

    def get(self, request):
        Form = SignInForm()
        print(Form)
        return render(request, 'signin.html', {'form':Form})

    def post(self, request):
        try:
            logout(request)
        except:
            pass
        Form = SignInForm(request.POST)
        if Form.is_valid:
            password = request.POST['password']
            email = request.POST['email']
        user = authenticate(email=email, password = password)
        if not user:
            error = 'Your email or Password is Incorrect'
        if user:
            login(request, user)
            return redirect('index')
        return render(request, 'signin.html', {'form':Form, 'error':error})

def LogoutHandle(request):
    logout(request)
    return redirect('signin')