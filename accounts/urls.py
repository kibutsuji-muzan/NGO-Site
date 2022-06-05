from django.urls import path
from accounts.views.signinview import *
from accounts.views.signupview import *

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
