from django.db import models


class Social(models.Model):

    social_networking = models.CharField(max_length=255, help_text="Use somente letras minusculas, e.g: facebook")
    profile = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s/%s" % (self.social_networking, self.profile)
