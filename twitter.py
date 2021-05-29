# Copyright Fastcoin Project 2021
# Get a developer key from developer.twitter.com

import tweepy
import time

# Consumer API Keys
auth = tweepy.OauthHandler('YOUR_API_KEY','YOUR_API_SECRET_KEY')

# Access tokens
auth.set_access_token('YOUR_ACCESS_TOKEN','YOUR_ACCESS_TOKEN_SECRET')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

# Keyword to search for
search = 'fastcoin'
# Number of instances to search for
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Interaction Successful')
# What interaction do you want from bot?  favorite? , retweet?
        tweet.favorite()
        time.sleep(60)
    except tweepy.TweetError as e:
        print(e.reason)
    except StopIteration:
        break
