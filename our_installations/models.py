from django.db import models


class OurInstallations(models.Model):

    photo = models.ImageField(upload_to="our_installation")
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "our installations"

    def __unicode__(self):
        return self.title
