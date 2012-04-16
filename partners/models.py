from django.db import models
from django.utils.translation import ugettext_lazy as _


class Partner(models.Model):

    name = models.CharField(max_length=255, verbose_name=_("name"))
    url = models.URLField()
    logo = models.ImageField(upload_to="partners")

    def __unicode__(self):
        return self.name
