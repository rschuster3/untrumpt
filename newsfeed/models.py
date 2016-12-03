from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Feed(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Name of this RSS feed (ex. BBC World News)"
    )
    url = models.URLField(
        max_length=250,
        help_text="URL of the RSS feed"
    )
    favicon = models.CharField(
        max_length=50,
        help_text="File name of favicon we're using; located in static/img/feed/favicons/"
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class FeedItem(models.Model):
    feed = models.ForeignKey(
        Feed
    )
    title = models.CharField(
        max_length=250,
        help_text="Title of the article"
    )
    url = models.URLField(
        max_length=250,
        help_text="URL of the article"
    )
    pub_date = models.DateTimeField(
        help_text="Datetime of article pub date in EST"
    )
    summary = models.TextField(
        help_text="Summary of the article"
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
