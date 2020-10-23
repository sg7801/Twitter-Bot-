import tweepy
import time
CONSUMER_KEY = 'added the consumer key'
CONSUMER_SECRET = 'added the consumer secret key'
ACCESS_KEY = 'added the access key'
ACCESS_SECRET = 'added the access secret key'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
search_word=['#coding','#programming','#c++','#SoftwareEngineering','#python']

for tweet in tweepy.Cursor(api.search, q=search_word,count=30,tweeet_mode='extended',lang='en').items(30):
    try:
        tweet.favorite()
        print("Liked the tweet from @"+tweet.user.screen_name)
        tweet.retweet()
        print("Retweeted the tweet.\n")
        time.sleep(77)
    except tweepy.TweepError as error:
        break
    except StopIteration:
        break

