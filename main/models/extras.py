from django.db import models
from django.utils.translation import gettext_lazy as _

class feedback(models.Model):

    name = models.CharField(_('Name'), max_length=20)
    email = models.EmailField(_('Email'), max_length=30)
    feedback = models.CharField(_('FeedBack'), max_length=300)

    def __str__(self):
        return self.name + '(' + self.email + ')' 