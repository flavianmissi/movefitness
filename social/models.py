from django.db import models
from django.utils.translation import ugettext_lazy as _


class Social(models.Model):

    social_networking = models.CharField(
        max_length=255,
        help_text="Use somente letras minusculas, e.g: facebook",
        verbose_name=_("social networking"))
    profile = models.CharField(max_length=255, verbose_name=_("profile"))

    def __unicode__(self):
        return "%s/%s" % (self.social_networking, self.profile)
