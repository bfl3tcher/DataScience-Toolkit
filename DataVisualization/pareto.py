def uniquePhoneLine_linetype_pareto(table, field1, field2):

    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline

    # set style
    plt.style.use('seaborn-whitegrid')

    # cumulative percent
    table['cum_percent'] = table[field1].cumsum() / table[field1].sum() * 100

    # set axis/plot info
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.bar(x = table[field2], height = table[field1], color = color_selected)

    ax2 = ax.twinx()
    ax2.plot(table[field2], table['cum_percent'], color = "black", marker = "D", ms = 7)
    ax2.yaxis.set_major_formatter(PercentFormatter())

    ax.tick_params(axis = "y", colors = 'black')
    ax2.tick_params(axis = "y", colors = "black")

    plt.title(fontweight ='bold')

    ax.set_xlabel('', fontweight = 'bold')
    ax.set_ylabel('', fontweight = 'bold')

    plt.xticks()

    plt.tight_layout()
    plt.show()
