'''
Linear Discriminant Analysis
- Script Components -
    - input data
    - select the target feature for LDA in LDA report function

- Brief Explainer -
- Purpose - feature extraction
    - LDA extracts features that best maximize differences amongst classes
    - Newly created features are found on this best seperation
- Combinations
    - LDA finds combinations of features that best seperate classes
    - PCA finds combinations of features that explain variance in the dataset
    - Factor analysis builds feature combinations on differences rather than similarities
- LDA works best when
    - Measurements of independent variables for each observation are continuous
    - Categorical data requires discriminant correspondance analysis instead
'''

## load library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


## load data
fn = ''
df = pd.read_csv(fn)


## LinearDiscriminantAnalysis Function
'''
Basic LDA function -
- inputs
    - source data
    - target/feature predicted/class to seperate for
- output
    - visualization of LDA components split amongst the target class
    - saved source data with linear discriminants appended as columns
    - output table explaining class weights with each discriminate
'''
def lda_model(table, target):

    ## analysis
    # dependencies
    data = table
    X = table.drop(target, axis=1).values
    y = table[target].values

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    scaled_data = sc.fit_transform(X)

    # Linear Discriminant Analysis
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    lda = LinearDiscriminantAnalysis(n_components=2)
    X_lda = lda.fit_transform(scaled_data, y)

    ## visualize results
    lda_visual(X_lda, y)

    ## return table
    lda_append(data, X_lda)

    ## report
    lda_report(data, lda, target)


## exporting file
def lda_append(table, lda_result):
    table['LD1'] = lda_result[:, 0]
    table['LD2'] = lda_result[:, 1]
    return table

## visualize result
def lda_visual(lda_result, target):

    ## visualization
    plt.figure(figsize=(12, 8))
    plt.scatter(
        lda_result[:, 0], lda_result[:, 1], c=target,
        cmap='rainbow', alpha=0.7, edgecolors='b'
    )
    plt.title('LDA - Component Seperation')
    plt.xlabel('LD1')
    plt.ylabel('LD2')
    plt.tight_layout()
    plt.show()

## report on components
def lda_report(table, lda, target):

    ## components table
    table = table.drop(target, axis=1)
    components = pd.DataFrame(lda.scalings_, columns=['LD1', 'LD2'],  index=table.drop('LD1', axis=1).drop('LD2', axis=1).columns)
    components_hl = components.style.format("{:.2}").background_gradient(cmap=('plasma'), axis=0)

    # export table
    import time
    todaysdate = time.strftime("%Y-%m-%d")
    components_hl.to_excel(todaysdate + '.LDA_Result' + '.xlsx')
    print('\nLD Components')
    print(components)

## function
lda_model(df, '')
