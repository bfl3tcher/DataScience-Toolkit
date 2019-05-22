'''
Linear Regression -
'''

'''
Import data for model
'''
# import libraries
import numpy as np
import pandas as pd


# import data
fn = ''    # filename
df = pd.read_csv(fn)    # save file as df




'''
Linear Model -

- General information
    - train test split (size = .3, random_state=101)
    - LinearRegression model fitting
    - Print - coefficients & intercept

- Simple Linear Regression - save one variable in features
- Multiple Linear Regression - save multiple vars in features
-- Remove or add as you test and evaluate the model --
'''



# features/predictors
features = []    # list of features - add one or multiple
X = df[features]    # save predictors as X


# target/prediction
target = ''    # target variable name
y = df[target]    # save taret as Y


# sklearn - train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.3, random_state=101)


# # standard scaler
# from sklearn.preprocessing import StandardScaler

# sc_X = StandardScaler()    # import standard scaler
# X_train = sc_X.fit_transform(X_train)    # scale X train
# X_test = sc_X.transform(X_test)    # scale X test


# hide runtime warnings - harmless bug
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")


# LinearRegression model
from sklearn.linear_model import LinearRegression    # linear regression model
lm = LinearRegression()    # instantiate Linear Regressor
lm.fit(X_train, y_train)    # fit training data to model

# # reporting
# print('Intercept', lm.intercept_)    # LM intercept

# cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])    # coefficients
# print('\n\t\tCoefficients\n\n', cdf)    # print dataframe of coefficients



'''
Modeling Results
- Plotting (Predicted values vs. Real values)
- Plotting (Residuals)
- Heatmap of correlations with the columns
'''
# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# graphing results
predictions = lm.predict(X_test)    # save predictions


'''
Model Evaluation - Metrics
-MAE - Mean Absolute Error
-MSE - Mean Squared Error
-RMSE - Root Mean Square Error
'''
# reporting metrics
from sklearn import metrics


# The coefficients
print('\n-----------------------------------------------------')
print('\tMetrics')
print('Intercept:', lm.intercept_)    # LM intercept
print('Variance score (R2): %.2f' % r2_score(y_test, predictions))
print('\n\tFeatures')
coef = pd.DataFrame(data=list(lm.coef_)[0], index=X.columns, columns=['Coef'])
print(coef.head())
print('\n-----------------------------------------------------')
print('MAE: ', metrics.mean_absolute_error(y_test, predictions))    # Mean Absolute Error
print('MSE: ', metrics.mean_squared_error(y_test, predictions))    # Mean Squared Error
print('RMSE: ', np.sqrt(metrics.mean_squared_error(y_test, predictions)))    # Root Mean Square Error
print('\n-----------------------------------------------------')


# graphing predicted vs actual
plt.scatter(x=predictions,y=y_test)
plt.title('Model Evaluation - Predicted vs. Actual')
plt.xlabel('Predicted')
plt.ylabel('Real')
plt.show()

# plotting residuals - difference between
# predicted and actual values
plt.title('Model Evaluation - Residuals')
residual = (y_test-predictions)
sns.distplot(residual)
plt.show()

# shows correlation with all the columns
sns.heatmap(df.corr(), cmap='coolwarm', annot=True)
plt.show()
