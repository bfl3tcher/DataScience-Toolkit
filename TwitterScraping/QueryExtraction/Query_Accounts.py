## Twython -J140 Tweet Downloader
'''
Twitter Scraping with Twython - Accounts

    -- Will scrape up to 100 tweets at a time per account
        - Must specify -
            - fn = filename exported
            - target_users = list of accounts to query
    -- Sentiment Analyzer excluded from this

'''
# set filename
fn = 'Tweets_Extracted_Accounts.csv'

# Target User Account
target_users = ["@FoxNews", "@nytimes", '@realDonaldTrump']


# import libraries
import Twitter_Credentials
import tweepy
import json as js
import pandas as pd
import numpy as np


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(Twitter_Credentials.CONSUMER_KEY, Twitter_Credentials.CONSUMER_SECRET)
auth.set_access_token(Twitter_Credentials.ACCESS_TOKEN, Twitter_Credentials.ACCESS_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Number of pages pulled
sentiments_DF = pd.DataFrame()
sentiments_dict = {}

for target_user in target_users:

    # Variables for holding sentiments
    sentiments = []
    pages = int(len(target_users))
    i=1

    # Counter
    counter = 1

    # Loop through 5 pages of tweets (total 100 tweets)
    for x in range(1,pages+1):

        # counting tweets made in order
        tweets_ago = counter

        # Get all tweets from home feed
        public_tweets = api.user_timeline(target_user, page = x)

        # Loop through all tweets
        for tweet in public_tweets:

            # Add sentiments for each tweet into an array
            array_dict = {"usr_user":target_user, "usr_id":tweet['user']['id'], "usr_user":tweet['user']['screen_name'], "usr_statuses":tweet['user']['statuses_count'], "usr_followers":tweet['user']['followers_count'], "usr_friends":tweet['user']['friends_count'], "usr_desc":tweet['user']['description'], "usr_profile_img":tweet['user']['description'], "usr_loc":tweet['user']['location'], "usr_start_date":tweet['user']['created_at'], "usr_bg_color":tweet['user']['profile_background_color'], "twt_id":tweet['id'], "twt_html":tweet['source'], "twt_text":tweet['text'], "twt_created":tweet['created_at'], "twt_retweets":tweet['retweet_count'], "twt_fav_count":tweet['favorite_count'], "twt_favorited":tweet['favorited'], "twt_quotestatus":tweet['is_quote_status'], "twt_reply_screenname":tweet['in_reply_to_screen_name'], "twt_reply_twtid":tweet['in_reply_to_status_id'], "twt_reply_userid":tweet['in_reply_to_user_id'], "twt_geo":tweet['geo'], "twt_inreply_name":tweet['in_reply_to_screen_name'], "twt_lang":tweet['lang'], "twt_truncated":tweet['truncated'], "twt_coord":tweet['coordinates'], "twt_hash":tweet['entities']['hashtags'],"Tweets Ago": tweets_ago}
            sentiments.append(array_dict)

            # Add to counter
            counter = counter + 1

    sentiments_dict[target_user] = pd.DataFrame.from_dict(sentiments)
    sentiments_dict[target_user]

    i += 1
    # Counter resets
    counter = 1


sentiments_DF = pd.concat(sentiments_dict,join_axes=None, ignore_index=True,keys=None, levels=None, names=None, verify_integrity=False)

# summary of dataframe
print(sentiments_DF.info())


# export dataframe to CSV file
sentiments_DF.to_csv(fn)
