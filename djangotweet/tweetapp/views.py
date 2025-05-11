from django.shortcuts import render

# Create your views here.

def listtweet(request):
    return render(request, 'tweetapp/listtweet.html')

def addtweet(request):
    return render(request, 'tweetapp/addtweet.html')

