## Twython -J140 Tweet Downloader
'''
Twitter Scraping with Twython - Hashtags

    -- Will scrape up to 100 tweets at a time
    -- Configure query settings to adjust parameters
            - defaults to most recent
            - must target hashtag
            - must specify date
    -- Hashtag variable targets which hashtag is searched
    -- Sentiment Analysis built in

'''
# setting start/end dates for query
pull_start = '2019-05-16'    # start date
pull_end = '2019-05-17'    # end date


# Hashtag being searched for
hashtags = ['#Trump']


# export filename
export_fn = 'tweets'+pull_start+'.csv'

# query submitted
query = {
    'q': hashtags,
    'count':100,
    'lang': 'en',
    'result_type':'recent',
    'tweet_mode':'extended',
    'since':pull_start,
    'until':pull_end,
}


'''
Extract Tweets
'''
# import libraries
import Twitter_Credentials
from twython import Twython
import json as js
import pandas as pd
import numpy as np


# import Twitter credentials
tweets = Twython(
Twitter_Credentials.CONSUMER_KEY,
Twitter_Credentials.CONSUMER_SECRET)


# Search tweets
dict_ = {'usr_id': [], 'usr_user': [], 'usr_statuses':[], 'usr_followers': [], 'usr_friends': [], 'usr_desc': [], 'usr_profile_img': [],'usr_loc': [], 'usr_start_date': [], 'usr_bg_color': [],'twt_id': [], 'twt_html': [], 'twt_text': [], 'twt_created': [], 'twt_retweets': [],'twt_retweeted': [], 'twt_fav_count': [],'twt_favorited': [],'twt_quotestatus': [],'twt_reply_screenname': [],'twt_reply_twtid': [],'twt_reply_userid': [],'twt_geo': [],'twt_inreply_name': [],'twt_lang': [],'twt_truncated': [],'twt_coord': [],'twt_hash': [],}


#  Tweet query - data structure
for status in tweets.search(**query)['statuses']:

    # user attributes
    dict_['usr_id'].append(status['user']['id'])
    dict_['usr_user'].append(status['user']['screen_name'])
    dict_['usr_statuses'].append(status['user']['statuses_count'])
    dict_['usr_followers'].append(status['user']['followers_count'])
    dict_['usr_friends'].append(status['user']['friends_count'])
    dict_['usr_desc'].append(status['user']['description'])
    dict_['usr_profile_img'].append(status['user']['description'])
    dict_['usr_loc'].append(status['user']['location'])
    dict_['usr_start_date'].append(status['user']['created_at'])
    dict_['usr_bg_color'].append(status['user']['profile_background_color'])

    # tweets
    dict_['twt_id'].append(status['id'])
    dict_['twt_html'].append(status['source'])
    dict_['twt_text'].append(status['full_text'])
    dict_['twt_created'].append(status['created_at'])
    dict_['twt_retweets'].append(status['retweet_count'])
    dict_['twt_retweeted'].append(status['retweet_count'])
    dict_['twt_fav_count'].append(status['favorite_count'])
    dict_['twt_favorited'].append(status['favorited'])
    dict_['twt_quotestatus'].append(status['is_quote_status'])
    dict_['twt_reply_screenname'].append(status['in_reply_to_screen_name'])
    dict_['twt_reply_twtid'].append(status['in_reply_to_status_id'])
    dict_['twt_reply_userid'].append(status['in_reply_to_user_id'])
    dict_['twt_geo'].append(status['geo'])
    dict_['twt_inreply_name'].append(status['in_reply_to_screen_name'])
    dict_['twt_lang'].append(status['lang'])
    dict_['twt_truncated'].append(status['truncated'])
    dict_['twt_coord'].append(status['coordinates'])
    dict_['twt_hash'].append(status['entities']['hashtags'])


# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(data=dict_)


# sentiment analysis tools
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# dataframe fed into sentiment analysis
col = ['usr_user', 'twt_text']    # columns
data_OE = df.loc[:, col]

data_OE = data_OE.fillna('0')

columns = []
for i in data_OE.columns:
    if i != 'usr_user':
        columns.append(i+'_cmp')
        columns.append('pos_%s'%i)
        columns.append('neg_%s'%i)
        columns.append('neu_%s'%i)

i = 0
df_dict = {}
for i in np.arange(len(columns)):
    for j in columns:
        df_dict[j]=[]

df_empty = pd.DataFrame(df_dict)
df_empty = df_empty[columns]

compound_list = []
positive_list = []
negative_list = []
neutral_list = []


i = 0;
for i in range(0,len(list(data_OE))-1):
    for text in data_OE.iloc[:,i+1]:

        # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(text)["compound"]
        pos = analyzer.polarity_scores(text)["pos"]
        neu = analyzer.polarity_scores(text)["neu"]
        neg = analyzer.polarity_scores(text)["neg"]

        # Add each value to the appropriate array
        compound_list.append(compound)
        positive_list.append(pos)
        negative_list.append(neg)
        neutral_list.append(neu)

    # print(compound_list)
    j = (i*4);
    k = (i*4)+1;
    l = (i*4)+2;
    m = (i*4)+3;
    df_empty.iloc[:,j] = compound_list
    df_empty.iloc[:,k] = positive_list
    df_empty.iloc[:,l] = negative_list
    df_empty.iloc[:,m] = neutral_list
    compound_list = []
    positive_list = []
    negative_list = []
    neutral_list = []

# merges sentiment results into dataframe
df = pd.merge(df,df_empty, left_index=True, right_index=True)


# export
# df_day.to_csv(export_fn, index=False)
df.head()
