from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def twitter_feed(request):
    return render(request, 'twitter_feed.html')


def about(request):
    return render(request, 'about.html')
