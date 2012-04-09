from django.db import models


class Activity(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "activities"

    def __unicode__(self):
        return self.title
