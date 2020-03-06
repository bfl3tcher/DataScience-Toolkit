'''
Correlation Test Params
- General Correlation Primer -
- https://www.statisticssolutions.com/correlation-pearson-kendall-spearman/

- Tests Available
    - 'pearson', 'kendall', 'spearman'
- pearson : standard correlation coefficient
    - Quick Reference -
    - best method of measuring the association between variables of interest
        because it is based on the method of covariance.
    - It gives information about the magnitude of the association,
        or correlation, as well as the direction of the relationship
    - https://www.statisticssolutions.com/pearsons-correlation-coefficient/
- Kendall and Spearman
    - kendall : Kendall Tau correlation coefficient
        - usually smaller values than Spearman’s rho correlation.
        - Calculations based on concordant and discordant pairs.
        - Insensitive to error.
        - P values are more accurate with smaller sample sizes
    - spearman : Spearman rank correlation
        - usually have larger values than Kendall’s Tau.
        - Calculations based on deviations.
        - Much more sensitive to error and discrepancies in data.
    - Quick Reference -
    https://www.statisticssolutions.com/kendalls-tau-and-spearmans-rank-correlation-coefficient/
'''
## correlation method
corr_method = 'pearson'
ex_fn = 'Corr_Mtx'


# libraries
import pandas as pd
import numpy as np
import scipy.stats as stats


# import data
fn = ''
df = pd.read_csv(fn)


'''
Correlation
- Exports Correlation Matrix
- Interactable Output Here
'''

def corr_matrix(table, test, fn):

    ## save correlations and tests
    corr = table.corr(method = str(test))
    corr_hl = corr.style.format("{:.2}").background_gradient(cmap=('viridis'), axis=1)

    ## export correlation
    import time
    todaysdate = time.strftime("%Y-%m-%d")
    corr_hl.to_excel(todaysdate + '.' + fn + '.xlsx')

    return corr_hl

## apply function
corr_matrix(df, corr_method, ex_fn)
