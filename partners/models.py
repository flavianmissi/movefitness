from django.db import models


class Partner(models.Model):

    name = models.CharField(max_length=255)
    url = models.URLField()
    logo = models.ImageField(upload_to="partners")

    def __unicode__(self):
        return self.name
