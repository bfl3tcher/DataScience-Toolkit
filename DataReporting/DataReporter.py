import pandas as pd

# load data
fn = '../zecon/Zip_time_series.csv'
df = pd.read_csv(fn)

print('BEGIN REPORT')

# print header of dataframe
print('\n-------------------------------------')
print('\n\tTopline Review\n')
print(df.head())


# print columns
print('\n-------------------------------------')
print('\tColumns:\n')
for i in df.columns:
    print(str(i))



# print descriptive stats
print('\n-------------------------------------')
print('\n\tDescriptive Summary Stats:')
for i in df.columns:
    print(i)
    print(df[i].describe())
    print('\n')


# print frequency counts
print('\n-------------------------------------')
print('\n\tFrequency Counts (top 10 results):')
for i in df.columns:
    print(i, '-TOTAL- ', df[i].count(),'\n')
    print(df[i].value_counts(dropna=False).head(10))
    print('\n')

print('\n-------------------------------------')
print('END OF REPORT')
