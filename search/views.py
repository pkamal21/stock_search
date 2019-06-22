from django.shortcuts import render
from .models import Query
from .forms import PostForm
from django.shortcuts import redirect
import tweepy as tw

consumer_key='BJDjBMEWm2DPuJDCPvdG2iyic'
consumer_secret='JbMC43uuyotJQoPt8hVdTlDEImBD0g82u9Dj9htJ4Z3DsF0W55'
access_token_key='1142026962250027008-WGrz5Ds7WaHcaL8qTF0aERQVvCiTxK'
access_token_secret='H2ffGEbSQS66OiXM7IEtywVuyLzR4o1TzxKO8KmFlVwDD'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# api.update_status("First tweet sent using the API !!!")



# Create your views here.

def query(request):
    queries = Query.objects.all()

    return render(request, 'search/query.html', {'queries':queries})


def result(request):
    return render(request, 'search/result.html')

def query_new(request):
    if request.method == 'POST':
        
        form = PostForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['query']
            new_search = " {} (share OR jump OR surge) -filter:retweets -filter:media".format(search)

            tweets = tw.Cursor(api.search,
                   q=new_search,
                   lang="en",
                   since='2018-04-23').items(10)

            all_tweets = [tweet.text for tweet in tweets]
            

            return render(request, 'search/result.html', {'all_tweets':all_tweets})
            
    else:
        form = PostForm()
        return render(request, 'search/query_edit.html', {'form':form})