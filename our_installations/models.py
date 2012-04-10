from django.db import models


class OurInstallation(models.Model):

    photo = models.ImageField(upload_to="our_installation")
    title = models.CharField(max_length=150)

    def __unicode__(self):
        return self.title
