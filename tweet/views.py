from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# Create your views here.


def tweet(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "tweet_list.html", {'tweets':tweets})


def tweet_create(request):

    if request.method == "POST" :
        form = TweetForm(request.Post, request.FILES)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else :
        form = TweetForm()
    return render(request, 'tweet_form' , {'form':form})


