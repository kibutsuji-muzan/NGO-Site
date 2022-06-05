from django.db import models
from accounts.models.ngouser import NGO_User
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    GENDER = [('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]

    name = models.CharField(_('Name'), max_length=20)
    email = models.EmailField(_('Email'), max_length=200, unique=True)
    phone = models.CharField(_('Phone Number'), max_length=200, null=True, blank=True)
    birthday = models.DateField(_('Birth Date'))
    gender = models.CharField(_('Gender'), max_length=6, choices=GENDER)
    user = models.OneToOneField(NGO_User, on_delete=models.CASCADE, verbose_name=_("User"))

    def __str__(self):
        full_name = self.first_name + self.last_name
        return full_name

class ProfileImage(models.Model):

    image = models.ImageField(_("Image"), upload_to="ProfileImages/", default="ProfileImages/default.png")
    alt_txt = models.CharField(_("Alternative Text"), max_length=20, default="Your Profile Image")
    created_at = models.DateTimeField(_("Created On"),auto_now=True,editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_("Profile"))
    
    class Meta:
        verbose_name = _("Profile Image")