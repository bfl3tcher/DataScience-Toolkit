# histogram function
def tid_histogram(table, field):

    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline

    # styling
    plt.style.use('seaborn-whitegrid')
    plt.subplots(figsize=(12, 8))

    # OVERALL DISTPLOT
    sns.distplot(table[field], bins = 10, kde = False, color = 'green', hist_kws=dict(edgecolor="k", linewidth=2),)

    # title
    plt.title('', fontweight = 'bold', fontsize = 13)
    plt.xlabel('', fontweight = 'bold')
    plt.ylabel('', fontweight = 'bold')

    plt.xticks(fontweight = 'bold')
    plt.yticks(fontweight = 'bold')

    plt.show()
