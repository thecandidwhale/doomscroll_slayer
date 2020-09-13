import tweepy
import os
import random
import time
from secrets import *

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_token_secret)

#print("hello world") #bot functions to this point

tweets = []

with os.scandir('./tweet_txt') as dirs:
    for entry in dirs:
        tweets.append(entry.name)

#print(tweets) bot can list txt files from folder

toSend = random.choice(tweets) #random can repeat which is not good for bot.
#how to fix?

print(toSend)
