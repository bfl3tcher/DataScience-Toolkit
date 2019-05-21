'''
Twitter Scraping with Tweepy - Accounts Query
    - Tweepy has specific tool for "search_users"
    - Built in, longer query required with Twython
    - Accept any list of accounts
        - iterate through most recent tweets
        - compile and build sentiment
    - Sentiment Analyzer built in
    - Extracts all available tweet data from Twitter
'''

# set filename
fn = 'Accounts_Sentiment.csv'

# Target User Account
target_users = ["@FoxNews", "@nytimes", '@realDonaldTrump']

# import libraries
import Twitter_Credentials
import tweepy
import json as js
import pandas as pd
import numpy as np


# Vader Sentiment analyses tool
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()



# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(Twitter_Credentials.CONSUMER_KEY, Twitter_Credentials.CONSUMER_SECRET)
auth.set_access_token(Twitter_Credentials.ACCESS_TOKEN, Twitter_Credentials.ACCESS_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())



# Number of pages pulled
sentiments_DF = pd.DataFrame()
sentiments_dict = {}
sentiments_means = {}
for target_user in target_users:

    # Variables for holding sentiments
    compound_list = []
    positive_list = []
    negative_list = []
    neutral_list = []
    sentiments = []
    sentiments_mean = []
    pages = int(len(target_users))
    i=1

    # Counter
    counter = 1

    # Loop through 5 pages of tweets (total 100 tweets)
    for x in range(1,pages+1):

        # Get all tweets from home feed
        public_tweets = api.user_timeline(target_user, page = x)

        # Loop through all tweets
        for tweet in public_tweets:
            # Run Vader Analysis on each tweet
            compound = analyzer.polarity_scores(tweet["text"])["compound"]
            pos = analyzer.polarity_scores(tweet["text"])["pos"]
            neu = analyzer.polarity_scores(tweet["text"])["neu"]
            neg = analyzer.polarity_scores(tweet["text"])["neg"]
            tweets_ago = counter

            # Add each value to the appropriate list
            compound_list.append(compound)
            positive_list.append(pos)
            negative_list.append(neg)
            neutral_list.append(neu)

            # Add sentiments for each tweet into an array
            array_dict = {"usr_user":target_user, "usr_id":tweet['user']['id'], "usr_user":tweet['user']['screen_name'], "usr_statuses":tweet['user']['statuses_count'], "usr_followers":tweet['user']['followers_count'], "usr_friends":tweet['user']['friends_count'], "usr_desc":tweet['user']['description'], "usr_profile_img":tweet['user']['description'], "usr_loc":tweet['user']['location'], "usr_start_date":tweet['user']['created_at'], "usr_bg_color":tweet['user']['profile_background_color'], "twt_id":tweet['id'], "twt_html":tweet['source'], "twt_text":tweet['text'], "twt_created":tweet['created_at'], "twt_retweets":tweet['retweet_count'], "twt_fav_count":tweet['favorite_count'], "twt_favorited":tweet['favorited'], "twt_quotestatus":tweet['is_quote_status'], "twt_reply_screenname":tweet['in_reply_to_screen_name'], "twt_reply_twtid":tweet['in_reply_to_status_id'], "twt_reply_userid":tweet['in_reply_to_user_id'], "twt_geo":tweet['geo'], "twt_inreply_name":tweet['in_reply_to_screen_name'], "twt_lang":tweet['lang'], "twt_truncated":tweet['truncated'], "twt_coord":tweet['coordinates'], "twt_hash":tweet['entities']['hashtags'], "Compound": compound, "Positive": pos, "Negative": neu, "Neutral": neg, "Tweets Ago": tweets_ago}
            sentiments.append(array_dict)

            # Add to counter
            counter = counter + 1

    sentiments_mean.append({"usr_user":target_user, "Mean Compound":np.mean(compound_list)})

    sentiments_dict[target_user] = pd.DataFrame.from_dict(sentiments)
    sentiments_dict[target_user]
    sentiments_means[target_user] = pd.DataFrame.from_dict(sentiments_mean)
    sentiments_means[target_user]

    i += 1
    # Counter resets
    counter = 1

# join appended dataframes together
mean_DF = pd.concat(sentiments_means,join_axes=None, ignore_index=True,keys=None, levels=None, names=None, verify_integrity=False)

sentiments_DF = pd.concat(sentiments_dict,join_axes=None, ignore_index=True,keys=None, levels=None, names=None, verify_integrity=False)


# summary of dataframe
print(sentiments_DF.info())


# export dataframe to CSV file
sentiments_DF.to_csv(fn)
