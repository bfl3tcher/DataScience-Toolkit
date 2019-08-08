''' P2P Functions '''

# event coding function
print('Loading Function')
def event_code(dataframe, column_source_name, new_column_name, loc_list, value):

    # terms list
    loc_list =  [x.lower() for x in loc_list]
    regex_string = '|'.join(loc_list)

    print('Coding -- ', str(new_column_name))
    locations = dataframe[str(column_source_name)]
    locations = locations.str.contains(str(regex_string), regex=True, na=False, case=False)

    dataframe.loc[locations, str(new_column_name)] = value

    dataframe[str(new_column_name)].fillna('Unlisted', inplace=True)

    print(str(new_column_name), 'Frequency Counts\n')
    print(dataframe[str(new_column_name)].value_counts(dropna=False))
    print('')


# column removal function
def col_cleaner(dataframe, columns_dropped):

    for var in columns_dropped:

        if var in dataframe.columns:
            print('REMOVED --', str(var))
            dataframe.pop(var)

        else:
            print('SKIPPED --', str(var))
