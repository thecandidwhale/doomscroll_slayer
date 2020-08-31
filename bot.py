import tweepy
import time
from secrets import *

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_token_secret)

#print("hello world") #bot functions to this point

with open('reminder.txt', 'r') as file:
    text = file.read()


#print(text) bot parses text correctly

twitter = tweepy.API(auth)

while True:
    time.sleep(1800)
    twitter.update_status(text)
