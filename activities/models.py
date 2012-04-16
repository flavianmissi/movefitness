from django.db import models
from django.utils.translation import ugettext_lazy as _


class Activity(models.Model):

    title = models.CharField(max_length=150, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = _("activities")

    def __unicode__(self):
        return self.title
