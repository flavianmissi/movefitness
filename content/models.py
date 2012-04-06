from django.db import models


class Content(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.title
