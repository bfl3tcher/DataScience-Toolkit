'''
Fuzzy Matching

- Partial matches words/phrases to text strings in column
- Function below will automatically create all available match types


- Not included
    - Filtering based on error rate
    - Selecting only a subset of match types


- Relevant Documentation
    - FuzzyWuzzy library docs
        - https://github.com/seatgeek/fuzzywuzzy

    - DataCamp intro guide - for reference
        - https://www.datacamp.com/community/tutorials

'''


'''
- Import libraries
- Load data
'''


# import pandas
import pandas as pd


# load file to memory
path = ''
df = pd.read_csv(path)


'''
Fuzzy Matching -

- fuzzymatch(dataframe, search_terms, source_columns)
    - dataframe = dataset being used
    - search_terms = terms you're fuzzy matching
    - source_columns = text columns being matched to list of terms

- outputs
    - ratio score -
    - partial score -
    - token sort -
    - token set -


'''


# import fuzzywuzzy library
from fuzzywuzzy import fuzz


# defining FuzzyMatch function
def fuzzymatch(dataframe, search_terms, source_column):

    # fuzzy match
    search_terms =  [x.lower() for x in search_terms]
    search_terms = '|'.join(search_terms)


    # fuzzy match application
    dataframe[str(source_column)].fillna("", inplace=True)

    ratio_score = []
    partial_ratio_score = []
    token_sort_ratio_score = []
    token_set_ratio_score = []


    for i, r in dataframe.iterrows():
        str1= r[str(source_column)]
        str2 = search_terms
        ratio = fuzz.ratio(str1.lower(),str2)
        ratio_score.append(ratio)

    dataframe['ratio_score'] = ratio_score

    for i, r in dataframe.iterrows():
        str1= r[str(source_column)]
        str2 = search_terms
        partial_ratio = fuzz.partial_ratio(str1.lower(),str2)
        partial_ratio_score.append(partial_ratio)

    dataframe['partial_ratio_score'] = partial_ratio_score

    for i, r in dataframe.iterrows():
        str1= r[str(source_column)]
        str2 = search_terms
        token_sort_ratio = fuzz.token_sort_ratio(str1.lower(),str2)
        token_sort_ratio_score.append(token_sort_ratio)

    dataframe['token_sort_ratio_score'] = token_sort_ratio_score

    for i, r in dataframe.iterrows():
        str1= r[str(source_column)]
        str2 = search_terms
        token_set_ratio = fuzz.token_set_ratio(str1.lower(),str2)
        token_set_ratio_score.append(token_set_ratio)

    dataframe['token_set_ratio_score'] = token_set_ratio_score

    return dataframe


'''
Applying FuzzyMatch function
'''


# specifying search terms
s_terms = ['', '', '']


# FuzzyMatch function
fuzzymatch(
    dataframe=,    # dataframe
    search_terms=s_terms,    # search terms used
    source_column=''    # column matched to terms
)


# exporting appended data
fn = 'FuzzyMatch.csv'
df.to_csv(fn)
