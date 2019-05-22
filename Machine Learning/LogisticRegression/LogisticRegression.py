'''
Logistic Regression
'''

'''
Import data for model
'''
# libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


# import data
fn = 'advertising.csv'    # filename
df = pd.read_csv(fn)    # save file as df



'''
Logistic Regression Model -

- General information
    - train test split (size = .3, random_state=101)
    - LinearRegression model fitting
    - Print - coefficients & intercept

- Simple Linear Regression - save one variable in features
- Multiple Linear Regression - save multiple vars in features
-- Remove or add as you test and evaluate the model --
'''


# features/predictors
features = ['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']    # list of features - add one or multiple
X = df[features]    # save predictors as X


# target/prediction
target = 'Clicked on Ad'    # target variable name
y = df[target]    # save taret as Y


# split training/test data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)


# # standard scaler
# from sklearn.preprocessing import StandardScaler

# sc_X = StandardScaler()    # import standard scaler
# X_train = sc_X.fit_transform(X_train)    # scale X train
# X_test = sc_X.transform(X_test)    # scale X test


# LogisticRegression model
from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()    # call LogisticRegressor
logmodel.fit(X_train,y_train)    # fit LR model

# predict test set
predictions = logmodel.predict(X_test)    # predict test set


'''
Model Evaluation
- Classification Report
- Confusion Matrix
- Coefficient printout
- CrossValidation Score
'''


from sklearn.metrics import classification_report, confusion_matrix

print('\n-----------------------------------------------------')
print('\tClassification Report')
print(classification_report(y_test,predictions))


print('\n-----------------------------------------------------')
print('\tConfusion Matrix')
print(confusion_matrix(y_test, predictions))


print('\n-----------------------------------------------------')
print('\tCoefficients')
coef = pd.DataFrame(data=list(logmodel.coef_)[0], index=X.columns, columns=['Coef'])
print(coef.head())


print('\n-----------------------------------------------------')
print('\tCrossValidation Score')
cross_val = pd.DataFrame(cross_validate(logmodel, X, y, cv=10, return_train_score=True))
print(cross_val)


'''
Logistic Regression - Curve Evaluation
- ROC AUC Score
- Plot ROC AUC Score
'''


print('\n-----------------------------------------------------')
print('ROC AUC Score (Area Under the Receiver Operating Characteristic Curve)')
from sklearn.metrics import roc_auc_score
roc_auc_score = roc_auc_score(y, logmodel.predict(X))    #
print(roc_auc_score)    #


print('\n-----------------------------------------------------')
from sklearn.metrics import roc_curve
false_positive_rate, true_positive_rate, thresholds = roc_curve(
    y, logmodel.predict(X))
plt.plot(false_positive_rate, true_positive_rate)
plt.xlabel('False Positives')
plt.ylabel('True Positives')
plt.title('ROC_AUC Curve')
plt.show()
