
import tweepy
import time

auth = tweepy.OAuthHandler('token ')
auth.set_access_token('access token')

api =tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user = api.me()
print('Your user name is:\t'+user.screen_name)

#choice=int(input('Enter 1 for getting list of followers\n2 for getting'))
#for follower in tweepy.Cursor(api.followers).items():
    #print(follower.name)

search='bayern'
nrTweets=5
for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('Tweet liked')
        tweet.favorite()
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break



    

