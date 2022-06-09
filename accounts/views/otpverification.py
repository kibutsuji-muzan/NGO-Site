from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.conf import settings
from django.core.mail import send_mail
from accounts.models.ngouser import NGO_User
from accounts.models.otpdevices import VerificationDevice
from django.views import View

# resend = False


class OtpVerification(View):

    def get(self, request):
        try:
            email = request.session['email']
            user = NGO_User.objects.get(email=email)
        except KeyError:
            return redirect('signup')
        else:
            totp = VerificationDevice.objects.get(user=user)
            print(totp)
            otp = totp.generate_challenge()
            message = f'hi sir, /n your otp for registration is {otp} for this email : {email}'
            subject = 'OTP verification mail'
            email_from = settings.EMAIL_HOST_USER
            to = [email,]
            send_mail(subject, message, email_from, to)
            print(otp)
        return render(request, 'otp.html')

    def post(self, request):
        try:
            email = request.session['email']
            user = NGO_User.objects.get(email=email)
        except:
            return redirect('signup')
        else:
            totp = VerificationDevice.objects.get(user=user)
            OTP = request.POST.get('otp')
            print(OTP)
            totp.verify_token(OTP)
            totp.refresh_from_db()
            if totp.verified:
                user.refresh_from_db()
                user.is_active = True
                user.save()
                login(request, user)
                return redirect('index')
            print(totp.verified)
            error = 'Wrong OTP or May Be Server Error'
        return render(request, 'otp.html', {'error':error})

def resendOTP(request):
    return redirect('OTP')