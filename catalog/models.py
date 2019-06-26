from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
import os

class Product(models.Model):

    pic = models.ImageField(upload_to='images/',blank=True, null=True)
    name = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    color = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.FloatField()


    def publish(self):
        self.published_date = timezone.now()

        self.save()

    @property
    def image_url(self):
        if self.pic and hasattr(self.pic, 'url'):
            return self.pic.url