from django.views import View
from django.shortcuts import render, redirect
from accounts.forms.signupform import SignUpForm

class SignUpView(View):

    def get(self, request):
        Form = SignUpForm()
        return render(request, 'signup.html', {'form':Form})

    def post(self, request):
        
        Form = SignUpForm(request.POST)
        if Form.is_valid():
            email = request.POST.get('email')
            user = Form.save()
            user.refresh_from_db()
            user.is_active = False

            user.save()
            request.session['email'] = email
            return redirect('otp')
        else:
            error = 'Correct Below Errors'
            print(Form.errors)
            return render(request, 'signup.html', {'form': Form, 'error':error})