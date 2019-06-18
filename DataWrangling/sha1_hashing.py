'''
Function for sha1 hashing
--- Only does sha1 hashing
  - replace sha1 below with diff has algorithm
    - hashlib.sha1()

-- Inputs for function -
--- currently requires input for all of these
    - dataframe = source dataframe
    - source_column = name of column being hashed
    - salt = code prepended to column that is hashed
    - new_column = name of column being created
'''
# import libraries
import hashlib
import pandas as pd


# load data
fn = ''
df = pd.read_csv(fn)


# hashing function
# specifies to sha1
def sha1_hash(dataframe, source_column, salt, new_column):
    # salt ad id
    salt = str(salt)    # apply salt
    dataframe[str(source_column)] = dataframe[str(source_column)].apply(lambda x: salt+x)    # set as column

    # create hash column
    dataframe[str(new_column)] = [hashlib.sha1(str.encode(str(i))).hexdigest() for i in dataframe[str(source_column)]]


sha1_hash(
    dataframe=ad_id,
    source_column='',
    salt='',
    new_column='')


ex_fn = ''
df.to_csv(ex_fn, index=False)
