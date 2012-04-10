from django.db import models
from django.utils.translation import ugettext_lazy as _


class OurInstallations(models.Model):

    photo = models.ImageField(upload_to="our_installation", verbose_name=_("photo"))
    title = models.CharField(max_length=150, verbose_name=_("title"))
    slug = models.SlugField()

    class Meta:
        verbose_name = _("our installations")
        verbose_name_plural = _("our installations")

    def __unicode__(self):
        return self.title
