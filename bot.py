import tweepy
from time import sleep
from secrets import *

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_token_secret)

#print("hello world") #bot functions to this point

twitter = tweepy.API(auth)

twitter.update_status("Hello World!")
