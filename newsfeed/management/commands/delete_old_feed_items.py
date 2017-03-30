import datetime
import pytz

from django.core.management.base import BaseCommand, CommandError

from newsfeed.models import FeedItem


est = pytz.timezone('US/Eastern')
utc = pytz.utc


class Command(BaseCommand):
    help = "Remove all news feed items older than one day to keep the database slim"

    def handle(self, *args, **options):
        for item in FeedItem.objects.all():
            if item.pub_date < utc.localize(datetime.datetime.now() - datetime.timedelta(days=1)).astimezone(est):
                item.delete()
