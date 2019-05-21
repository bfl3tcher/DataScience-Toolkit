'''
VADER - Sentiment Analysis tool
    - Open source tool for sentiment Analysis
    - Takes input file with text columns
    - Returns POS/NEG/NEUTRAL/COMP scores
        - refer to VADER docs on git for more info
        
    - Variables to use
        - fn = the filename and path of imported file
        - col = targets columns analyzed
            - unique row id
            - text columns
        - export_fn = filename exported
    -
'''


import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

'''
Setting filenames --
    - fn = the filename and path of imported file
    - export_fn = filename exported
'''
# setting filenames
fn = ''    # imported filename
export_fn = ''    # exported filename


# save imported data to dataframe
df = pd.read_csv(fn)


'''
Targeted columns --
- col = targets columns analyzed
    - unique row id
    - text columns
'''
# dataframe fed into sentiment analysis
col = ['user', 'text']    # columns
data_OE = df.loc[:, col]


'''Vader Sentiment Analyzer
- no changes necessary
- takes previous inputs
    -> then merges with imported file
'''
analyzer = SentimentIntensityAnalyzer()

data_OE = data_OE.fillna('0')

columns = []
for i in data_OE.columns:
    if i != 'user':
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


# save processed file
df.to_csv(export_fn, index=False)
