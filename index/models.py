from django.db import models


class Image(models.Model):

    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="index_images")

    def __unicode__(self):
        return self.description
