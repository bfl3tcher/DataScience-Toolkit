'''
K Nearest Neighbors (KNN) with scikit-learn
'''

'''
Load and import data
'''

# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


# load data
fn = './'
df = pd.read_csv(fn, index_col=0)


# set predicted feature
target = ''
knn_num = '15'


'''
Scaling features and predictors
'''

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df.drop(target, axis=1))
scaled_features = scaler.transform(df.drop(target, axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1], )


'''
Modeling
'''
# split train/test data
from sklearn.model_selection import train_test_split
X = df_feat
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)


# KNN
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=int(knn_num))

knn.fit(X_train, y_train)

pred = knn.predict(X_test)


'''
Model Evaluation
'''
print('\n-----------------------------------------------------')
print('\tAccuracy Score')
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))

print('\n-----------------------------------------------------')
print('\tConfusion Matrix')
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, pred))

print('\n-----------------------------------------------------')
print('\tClassification Report')
from sklearn.metrics import classification_report
print(classification_report(y_test, pred))


'''
Graphing Error
'''
error_rate = []

for i in range(1, 60):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

print('\n-----------------------------------------------------')
print('\tError Rate Report')
plt.figure(figsize=(10,8))
plt.plot(
    range(1,60),
    error_rate,
    color='red',
    linestyle='dashed',
    marker='o',
    markerfacecolor = 'blue',
    markersize=10)
plt.title('Error Rate vs K Value')
plt.ylabel('Error Rate')
plt.xlabel('K value')
plt.show()
