from django.shortcuts import render
from . import models

# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render(request, 'tweetapp/listtweet.html',context=tweet_dict)

def addtweet(request):
    return render(request, 'tweetapp/addtweet.html')

