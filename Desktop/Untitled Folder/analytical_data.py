import numpy as np
import matplotlib.pyplot as plt
import pandas as  pd
train = pd.read_csv('train.csv')
test = pd.read_csv('train.csv')

X_train = train.drop(["price_range"],axis=1)
y_train = train["price_range"]

#print(train.columns)
#print(train.head())

#train.info()
#train.describe()

import statsmodels.api as sm
SL = 0.05
X_train_arr=X_train.values
X_opt = X_train_arr[:, [0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]
X=np.append(arr=np.ones((2000,1)).astype(int),values=X_train,axis=1)
regressor_ols=sm.OLS(endog=y_train,exog=X_opt).fit()

print(regressor_ols.summary())
li=[]
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y_train, x).fit()
        maxVar = max(regressor_OLS.pvalues)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j] == maxVar):
                    x = np.delete(x, j, 1)
                    li.append(j)
    regressor_OLS.summary()
    return x
X_Modeled = backwardElimination(X_opt, SL)
test=test.values
test=np.delete(test,5,1)
test=np.delete(test,6,1)
test=np.delete(test,12,1)