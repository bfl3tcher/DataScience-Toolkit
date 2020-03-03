def linetype_stackedbar(table):

    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline


    # set style
    plt.style.use('seaborn-whitegrid')
    # color_list = ['darkgreen', 'olivedrab', 'orangered', 'indianred', 'firebrick', 'maroon']

    ## make stacked bar chart
    # plot chart
    table.plot(kind='bar', figsize=(12, 8), stacked=True, fontsize = 11, edgecolor = 'Black')

    # title / labels / ticks
    plt.title(fontweight = 'bold', fontsize = 13)

    plt.ylabel(fontweight = 'bold')
    plt.yticks(fontweight ='bold')

    plt.xlabel('')
    plt.xticks(fontweight = 'bold', rotation = 'horizontal')

    plt.legend(loc='upper center', bbox_to_anchor = (.5, 1.01), shadow = False, ncol = len(table.columns))
    plt.tight_layout()
    plt.show()
