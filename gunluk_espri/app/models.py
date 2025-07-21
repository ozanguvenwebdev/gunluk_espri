from django.db import models
import datetime
import time
from datetime import datetime, date, time, timedelta
from django.contrib.auth.models import User

# Create your models here.

def return_date_time():
    now = datetime.now() + timedelta(hours=3)
    return now


class Profile(models.Model):

    user            = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True,verbose_name="User Model", related_name='access_profile')
    name            = models.CharField(max_length=200, null=True, blank=True,verbose_name="Profile Name")
    surname         = models.CharField(max_length=200, null=True, blank=True,verbose_name="Profile Surname")
    description     = models.CharField(max_length=150, null=True, blank=True,verbose_name="Profile Description")
    email           = models.EmailField(max_length=200, null=True, blank=False)
    date_created    = models.DateTimeField(default=return_date_time, verbose_name='Profile Creation Date',null=True, blank=True,)
    notified        = models.BooleanField(blank=True, null=True, default=False, verbose_name="Subscribed?")
    active          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Active?")

    def __str__(self):
        return self.user.username


class Tweet(models.Model):
    
    content         = models.TextField(null=True, blank=True, verbose_name="Tweet")
    profile         = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    url_name        = models.SlugField(max_length=500, blank=True, help_text='This will be filled automatically', verbose_name='Sayfa Uzantısı')
    active          = models.BooleanField(blank=True, null=True, default=True, verbose_name="Kullan")
    create_date     = models.DateField(default=return_date_time, verbose_name='Tarih')
    order           = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Sıralama')

    class Meta:
        verbose_name_plural = "Tweets"
        verbose_name = "Tweet"
        ordering = ['-order']

    def __str__(self):
        return self.content