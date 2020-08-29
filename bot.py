import tweepy
from time import sleep
from secrets import *

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set _access_token(a_token, a_token_secret)
api = tweepy.API(auth)

tweet_text = "This is a friendly reminder to make sure you're not doomscrolling."

def tweet():
        for line in file_lines:
            try:
                api.update_status(tweet_text)
                sleep(1800)

tweet()
