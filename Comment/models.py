from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
class Utwor(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    song = models.FileField()
    IloscWyswietlen = models.DecimalField(max_digits=20,decimal_places=0,default=Decimal('0'))
    imgurl = models.CharField(max_length = 200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

