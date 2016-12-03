from django.shortcuts import render

from newsfeed.models import FeedItem


def newsfeed(request):
    context_variables = {}

    # All items from RSS feeds for the last 3 days
    feed_items = FeedItem.objects.all().order_by('-pub_date')[:50]

    context_variables['feed_items'] = feed_items

    return render(request, 'newsfeed/newsfeed.html', context_variables)
