from django.db import models
from django.utils.translation import ugettext_lazy as _


class Content(models.Model):

    title = models.CharField(max_length=255, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))
    slug = models.SlugField()

    def __unicode__(self):
        return self.title
