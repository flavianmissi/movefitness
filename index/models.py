from django.db import models
from django.utils.translation import ugettext_lazy as _


class Image(models.Model):

    description = models.CharField(max_length=255, verbose_name=_("description"))
    photo = models.ImageField(upload_to="index_images", verbose_name=_("photo"))

    class Meta:
        verbose_name_plural = _("images")

    def __unicode__(self):
        return self.description
