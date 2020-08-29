import tweepy
from secrets import *

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set _access_token(a_token, a_token_secret)
api = tweepy.API(auth)

tweet = "This is a friendly reminder to make sure you're not doomscrolling."

api.update_status(tweet)
