import datetime

from django.core.management.base import BaseCommand, CommandError

from newsfeed.models import FeedItem


class Command(BaseCommand):
    help = "Remove all news feed items older than one day to keep the database slim"

    def handle(self, *args, **options):
        for item in FeedItem.objects.all():
            if item.pub_date < (datetime.datetime.now() - datetime.timedelta(days=1)):
                item.delete()
