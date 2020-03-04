'''
Logistic Regression
- Brief Explainer -
- Purpose -
    - Classification algorithm that predicts an outcome (DV) based on one or more combinations of predictors (IVs)
    - Predictor is a binary class, and IVs are what best predicts outcome in that binary class
    - Generates weights and coefficients for the model to predict new outcomes
- Assumptions -
    - DV must be binary
        - ordinal log regression requires DV to be ordinal
    - Observations must be independent, not from repeated or matched data
    - No multicolinearity among IVs, and not too correlated with one another
    - linearity of IV is assumed - linearity of IVs is related to log odds
- Regularization Primer -
    - regularization adds bias to prevent overfitting or underfitting data
    - cost function adds contraints to control strength of regularization


- Model Performance
- Evaluation Metrics/Reports
- Scores
    - Score - mean accuracy of the test data and labels
    - AUC - area that exists under the ROC Curve - roughtl amount of data correctly identified
- Confusion Matrix - table of actual vs. predicted values of the model
- Classification Report
    - Accuracy - (True Positives + True Negatives) / (all possible outcomes)
    - Sensitivity - (True Positives) / (True positives & False negatives)
    - Specifity - True Negatives / (True negatives & False positives)
- ROC Curve -
    - Receiver Operating Characteristic Curve -
    - Area Under Curve of ROC provides measure of the model's fit
    - Tradeoff between sensitivity and specificity (increases in one, decreases the other)
    - The tighter the curve is on the left-hand border, the more accurate the test
    - Closer to curve comes to the 45-degree diagonal of the ROC space, less accurate the test


- Parameters -
- Solvers -
    - newton-cg
        - newton method
        - slow for large datasets, computes second derivatives
    - lbfgs - New default solver
        - Limited-memory Broyden–Fletcher–Goldfarb–Shanno
        - approximates second derivative matrix with gradient evaluations
        - Stores last few updates to save memory, not super fast with large datasets
    - liblinear - Older default solver
        - Large Linear Classification
        - Coordinate descent algorithm based on minimizing multivariate function by solving univariate optimization problems
        - Moves toward minimum in one direction at a time - works well in high dimensions
        - Drawbacks
            - Unable to run in parallel
            - Only solve mutli-class logistic regression with one vs. rest
    - sag -
        - Stochastic Average Gradient descent
        - Gradiant descent and incremental aggregated gradient approaches using random sample of previous gradient values
        - Fast for big datasets
    - saga -
        - Stochastic Average Gradient descent with L1 regularization
        - Generally trains faster than sag
- penalty - assigns regularization method, default is L2, "None" leads to no regularization
    - l1 - Lasso Regression
        - encourages simple and sparse models (fewer parameters), fewer coefficients
        - better for interpretability
        - supported by - liblinear, saga
    - l2 - Ridge Regression
        - larger and complicated models, reduces magnitude of all coefficients
        - all coefficients are shrunk by the same factor, will not result in sparse
        - better for including all data points and maintaining accuracy
        - supported by - newton-cg, sag, lgfgs
    - elasticnet
        - supported by - saga
    - None
- class_weight -
    - feed dictionary with labels and weights to more directly weight one class over another
    - "balanced" gives all classes equal weight inversely related by how prevalent it is
'''


# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


# load data
fn = ''
df = pd.read_csv(fn)


## logistic regression function
def logReg_model(x, y):

    # set table copy
    table = x.copy()

    # select X and y values
    X = x.values
    y = y.values

    # split training and test data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # feature scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)


    # Fitting Logistic Regression to the Training set
    from sklearn.linear_model import LogisticRegression
    logreg = LogisticRegression(random_state = 42, solver='lbfgs', multi_class='auto')
    logreg.fit(X_train, y_train)


    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # reporting
    logReg_report(logreg, table, X_test, y_test, y_pred)

    ## MODEL VISUALIZATION
    print('\n\t----MODEL VISUALIZATION----')
    logReg_auc_viz(y_test, y_pred)
    logReg_visualization(X_train, y_train, '(Train Set)')
    logReg_visualization(X_test, y_test, '(Test Set)')


## model metrics
def logReg_report(model, table, xtest, ytest, ypred):

    ## model scores
    # AUC/ROC Curve and Score
    print('--Area Under Curve of ROC Curve--')
    from sklearn.metrics import roc_auc_score
    roc_auc_score = roc_auc_score(ytest, model.predict(xtest))
    print(roc_auc_score, '\n')

    # predictor coefficients
    print('--Predictor Coefficients--')
    coefficients = pd.DataFrame(model.coef_, columns=table.columns, index=['Coeff'])
    coefficients = coefficients.T
    print(coefficients, '\n')

    # confusion matrix
    print('--Confusion Matrix--')
    from sklearn import metrics
    conf_matrix = metrics.confusion_matrix(ytest, ypred)
    print(conf_matrix, '\n')

    # classification report
    print('--Classification Report--')
    class_report = metrics.classification_report(ytest, ypred)
    print(class_report, '\n')


## visualizing training_test set
def logReg_visualization(X_set, y_set, set_type):
    from matplotlib.axes._axes import _log as matplotlib_axes_logger
    matplotlib_axes_logger.setLevel('ERROR')

    from matplotlib.colors import ListedColormap
    X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01), np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
    plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),alpha = 0.75, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())

    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(
            X_set[y_set == j, 0], X_set[y_set == j, 1],
            c = ListedColormap(('red', 'green'))(i), label = j
        )
    plt.title('Logistic Regression ' + str(set_type))
    plt.xlabel('Predictor')
    plt.ylabel('Target')
    plt.legend()
    plt.show()

## model visualization
def logReg_auc_viz(ytest, ypred):

    from sklearn.metrics import roc_curve, auc
    fpr, tpr, thresholds = roc_curve(ytest, ypred)
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")

    plt.tight_layout()
    plt.show()

## apply model
logReg_model(x = , y = )
