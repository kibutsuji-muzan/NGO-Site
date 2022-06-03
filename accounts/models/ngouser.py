from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.manager import NGO_UserManager
from django.utils import timezone
from accounts.models.subscriptions import SubscriptionType

class NGO_User(AbstractUser):
    # SUBSCRIPTIONS = [('SILVER','SILVER'),('GOLD','GOLD'),('PLATINUM','PLATINUM'),('FREE','FREE')]
    GENDER = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]
    username = None
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    first_name = models.CharField(_("First Name"),max_length=30, blank=True)
    last_name = models.CharField(_("Last Name"),max_length=30, blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=12, unique=False, blank=True)
    # subscription = models.CharField(_('Subscription'), max_length=8, choices=SUBSCRIPTIONS, default='FREE')
    subscription = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE, verbose_name='Subscription Type', blank=True, null=True)
    gender = models.CharField(_('Gender'),choices=GENDER, max_length=6, blank=True)
    birthday = models.DateField(_('Birth Date'), default=timezone.now, blank=True)
    created_at = models.DateTimeField(auto_now=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    object = NGO_UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class LoggedInUser(models.Model):
    user = models.OneToOneField(NGO_User,verbose_name=_("User") ,related_name='logged_in_user', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, null=True, blank=True,verbose_name=_("Session Key"))
    user_agent = models.SlugField(max_length=255,null=True, blank=True,verbose_name=_("User Agent"))
    client_ip = models.SlugField(max_length=255,null=True, blank=True,verbose_name=_("Client IP"))

    def __str__(self):
        return self.user.email

