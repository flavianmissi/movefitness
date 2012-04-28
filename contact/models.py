from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):

    address = models.CharField(max_length=350, verbose_name=_("address"))
    phone = models.CharField(max_length=50, verbose_name=_("phone"))
    business_hours = models.TextField(verbose_name=_("business hours"))

    class Meta:
        verbose_name_plural = _("contacts")

    def __unicode__(self):
        return self.address
