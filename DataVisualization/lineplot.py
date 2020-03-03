def totaltnx_lineplot(table):

    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline


    # set style
    plt.style.use('seaborn-whitegrid')

    # set color_list
    # color_list = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:cyan', 'tab:pink', 'tab:gray', 'tab:olive', 'coral', 'chartreuse', 'lavender', 'lightblue', 'violet', 'maroon',]

    # plot
    plot = table.plot(kind = 'line', figsize = (12, 8), fontsize = 11, linewidth = 4)

    # title / labeling
    plt.title('', fontweight = 'bold', fontsize = 13)

    plt.xlabel('', fontweight = 'bold')
    plt.xticks(fontweight = 'bold', rotation = 'vertical')

    plt.ylabel('', fontweight = 'bold')
    plt.yticks(fontweight ='bold')

    # legend plot formatting
    plt.legend(loc='upper center', bbox_to_anchor=(.5, 1.01), shadow=True)
    plt.tight_layout()

    plt.show()
