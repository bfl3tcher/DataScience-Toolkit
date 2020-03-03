def date_format(table, date_col):

    # create dt object
    table['Date'] = pd.to_datetime(table[date_col], infer_datetime_format=True)

    # create time objects for manipulation
    table['Calendar_Date'] = table['Date'].dt.date
    table['Month'] = table['Date'].dt.week
    table['Week'] = table['Date'].dt.week
    table['Month'] = table['Date'].dt.month
    table['dayofyear'] = table['Date'].dt.dayofyear
    table['hour'] = table['Date'].dt.hour
    table['year'] = table['Date'].dt.year
