import feedparser
import pytz
from time import mktime
import datetime

from django.utils.html import strip_tags
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.date import DateTrigger

from newsfeed.models import Feed, FeedItem


sched = BlockingScheduler()
est = pytz.timezone('US/Eastern')
utc = pytz.utc


@sched.scheduled_job('interval', hours=1)
def update_newsfeed():
    for feed in Feed.objects.all():
        feed_data = feedparser.parse(feed.url)
        for entry in feed_data.entries:
            pub_datetime = datetime.datetime.fromtimestamp(mktime(entry.published_parsed))
            pub_localized = utc.localize(pub_datetime)
            pub_eastern = pub_localized.astimezone(est)
            if not FeedItem.objects.filter(title=entry.title.encode('ascii','ignore')):
                FeedItem.objects.create(
                    feed=feed,
                    title=entry.title.encode('ascii','ignore'),
                    url=entry.link,
                    summary=strip_tags(entry.summary.encode('ascii','ignore')),
                    pub_date=pub_eastern
                )


@sched.scheduled_job('interval', days=3)
def remove_old_feed_items():
    for item in FeedItem.objects.all():
        if item.pub_date < (datetime.datetime.now() - datetime.timedelta(days=3)):
            item.delete()


sched.add_job(func=update_newsfeed,
              trigger=DateTrigger(run_date=datetime.datetime.now()))
sched.start()
