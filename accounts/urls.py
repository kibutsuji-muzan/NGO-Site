from django.urls import path, include
from accounts.views import signinview, signupview, otpverification, passwordreset
from django.contrib.auth import views as auth_views

passwordpatterns = [
    # password reset urls
    path('', passwordreset.PasswordResetView.as_view(), name='resetrequest'),
    path('done/', auth_views.PasswordResetDoneView.as_view(template_name='password/passwordresetdone.html'), name='passwordresetdone'),
    path('confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/passwordresetconfirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/passwordresetcomplete.html'), name='password_reset_complete'),
]

urlpatterns = [
    path('signin/', signinview.SignInView.as_view(), name='signin'),
    path('signup/', signupview.SignUpView.as_view(), name='signup'),
    path('logout/', signinview.LogoutHandle, name='logout'),
    path('otp/', otpverification.OtpVerification.as_view(), name='otp'),
    path('resend/', otpverification.resendOTP, name='resendrequest'),
    # password rsetpattern
    path('passwordreset/', include(passwordpatterns))

]