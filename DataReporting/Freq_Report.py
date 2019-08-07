''' Load library and data '''
# import library
import pandas as pd

# import dataframe
fn = ''
df = pd.read_csv(fn)



''' set functions  '''
# report functions
def var_report(dataframe, var):

    # var name
    print('Variable - ' + str(var) + '\n')

    # total unique
    unique = dataframe[var].nunique()
    print('# Unique - ' + str(unique))

    # total count
    total = dataframe[var].count()
    print('# Total - ' + str(total))

    # value counts
    if unique < 25:
        print('\n' + str(var) + ' FREQUENCY TOTALS - VERBOSE')
        print(dataframe[var].value_counts(dropna=False))
        print('----------')

    elif unique > 25:
        print('\n' + str(var) + ' FREQUENCY TOTALS - top 20')
        print(dataframe[var].value_counts(dropna=False).head(20))
        print('----------')




def freq_report(dataframe):

    for var in dataframe.columns:

        var_report(dataframe, var)



''' Call and print report functions '''
freq_report(dataframe)
