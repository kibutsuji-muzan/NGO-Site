from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

class SubscriptionType(MPTTModel):

    name = models.CharField(_('Name'), max_length=10)
    rate = models.IntegerField(_('Cost'))
    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _("SubscriptionType")
        verbose_name_plural = _("SubscriptionTypes")

    def __str__(self):
        return self.name

class DetailPoint(models.Model):
    name = models.CharField(_('Name'),max_length=20)

    def __str__(self):
        return self.name

class DetalPointValue(models.Model):
    detail = models.ForeignKey(DetailPoint, verbose_name=_('Point'), on_delete=models.CASCADE)
    value = models.CharField(_('Value'),max_length=20)
    subs = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name