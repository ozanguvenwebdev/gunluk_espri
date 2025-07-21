from django.contrib import admin
from app.models import *
# Register your models here.

class AdminTweet(admin.ModelAdmin):
    list_display = ( "content","profile","order","create_date","active",)
    search_fields = ["content"]
    list_editable = ('order','active')
    prepopulated_fields = {"url_name": ("content",)}
admin.site.register(Tweet,AdminTweet)

class AdminProfile(admin.ModelAdmin):
    list_display = ('name','surname','user','email')
admin.site.register(Profile, AdminProfile)