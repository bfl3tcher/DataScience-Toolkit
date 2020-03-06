'''
Principle Components Anaylsis
- Script Components -
-

- Brief Explainer -
- Purpose
    - PCA decreases model complexity by isolating combinations of features that explain variance in the data
    - Maximizes total variance for patterns
- Categorical
    - PCA was designed for continuous and scaled variables - interval and ratio
    - PCA will run for categorical variables, but other dimensionality reduction methods are preferable
- Scaling
    - PCA is sensitive to scaling, so features must be scaled before they can be calculated
    - Absence of scaling with skew how PCA explains the variance in the data
'''
## script parameters feature
num_components = 8
export_filename = 'PCA_Results'

## load libraries/data
# libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# data
fn = '../Test_Data/Wine.csv'
df = pd.read_csv(fn)


## pca function
'''
Basic PCA function -
- purpose
    - data exploration and mining
    - not ready to be fed into model directly
- inputs
    - table = data source for analysis
    - num_comp = number of components to find
    - filename = saved name of table
- output
    - export Excel file of component results
    - return table in view for Jupyter
'''
def pca_model(table, num_comp, fn):

    X = table.values

    ## scaling - import scaling, fit to data
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    sc.fit(X)
    scaled_data = sc.transform(X)

    ## PCA - analysis
    from sklearn.decomposition import PCA
    pca = PCA(n_components=int(num_comp))
    X_pca = pca.fit_transform(scaled_data)

    ## Table of Components
    components = pd.DataFrame(pca.components_, columns=table.columns)
    components = components.T
    components_hl = components.style.format("{:.2}").background_gradient(cmap=('plasma'), axis=0)

    # export table
    import time
    todaysdate = time.strftime("%Y-%m-%d")
    components_hl.to_excel(todaysdate + '.' + fn + '.xlsx')

    return components_hl


## function
pca_model(df, num_components, export_filename)
