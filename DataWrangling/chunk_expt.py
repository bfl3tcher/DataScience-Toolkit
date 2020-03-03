'''
Chunk Processing/Export for large data files
- Specifications -
    - filename - will use this for export filename - should be gzip compressed
    - fn_salt - added phrase to make output files distinct
    - chunk_sz - size of chunks used in processing
    - col - column names to add

- Output -
    - Several chunk files
    - gzip compressed
    - Will iterate and add number to filename
'''

## specification for script
fn = ''
fn_salt = ''
chunk_sz = 2 * (250000)
col = []


## script
# import pandas
import pandas as pd
import itertools

# processing in chunks
print('Loading ' + fn)
for chunk, it in zip(pd.read_csv(fn, compression = 'gzip', chunksize = chunk_sz, low_memory=False), itertools.count()):

    # Neustar account recode
    print(chunk.shape)

    # insert function here to process data as it's being loaded into chunks

    # set and print filename for chunk sample
    ex_fn = 'S'+ str(it + 1) + str(fn_salt) + fn
    print(ex_fn)
    chunk.to_csv(ex_fn, chunksize = chunk_sz, index=False)
