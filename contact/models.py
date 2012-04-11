from django.db import models


class Contact(models.Model):

    address = models.CharField(max_length=350)
    phone = models.CharField(max_length=50)
    business_hours = models.TextField()
