import tweepy
import os
import random
import time
from secrets import *

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_token_secret)

#print("hello world") #bot functions to this point

line = random.choice(open('slayers.txt').readlines())

print(line)
