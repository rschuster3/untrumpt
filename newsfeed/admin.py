from django.contrib import admin
from .models import *

class FeedAdmin(admin.ModelAdmin):
    search_fields = ['name']


class FeedItemAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedItem, FeedItemAdmin)
