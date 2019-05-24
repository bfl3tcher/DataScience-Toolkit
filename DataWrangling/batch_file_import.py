'''
Batch Importing Files
- Import and merge all CSV files in a folder

- Stack order 
    - set path below
    - imports all CSV files in path folder
    - merges together into one dataframe

- automatically set todo
    - Ignore Index of dataframes
    - Maintain column header order
    - exports merged files as "BatchedFiles.csv"
'''

# import libraries
import pandas as pd
import numpy as np
import os
import glob

# import all CSV files in path
path = r'/filepath/filepath/filepath'    # set filepath
all_files = glob.glob(os.path.join(path, "*.csv"))

# save files as dataframes
df = (pd.read_csv(f) for f in all_files)    # read files in path
df = pd.concat(df, ignore_index=True, sort=False)    #

# export files
export_name = 'BatchedFiles.csv'
df.to_csv(export_name)
