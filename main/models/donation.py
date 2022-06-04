from django.db import models
from django.utils.translation import gettext_lazy as _

class donation(models.Model):
    donator_name = models.CharField(_('Donator Name'), max_length=20, blank=True, null=True)
    address = models.CharField(_('Address'), max_length=40, blank=True, null=True)
    doanted_money = models.IntegerField(_('Money Donated'), blank=True, null=True)
    phone = models.CharField(_('Phone Number'), blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=30, blank=True, null=True)
    donated_on = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.email + '(' + self.donator_name + ')'