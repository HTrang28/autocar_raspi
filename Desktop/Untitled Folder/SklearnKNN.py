import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import tensorflow as tf
#from sklearn.model_selection import train_test_split
#from keras.utils import to_categorical
#from keras.models import Sequential, load_model
#from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout

"""Train and test in train folder"""

train_value = pd.read_csv('train.csv')
#print(df.shape)
#print(df.head())

X =train_value[['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc',
       'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi']].values
Y = train_value['price_range'].values

p = np.random.permutation(len(X))
x_train = X[p[:int(0.8*len(X))]].copy()
y_train = Y[p[:int(0.8*len(X))]].copy()

x_test = X[p[int(0.8*len(X)):]].copy()
y_test = Y[p[int(0.8*len(X)):]].copy()

print(x_train.shape)
print(y_train.shape)

'''train by KNN model'''
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(5)
knn.fit(x_train, y_train)

'''test'''
output = knn.predict(x_test)

for i in range(10):
    print("Output = {0}, Y_test = {1}".format(output[i], y_test[i]))

print('khac',len(output[output != y_test]))

'''plot output and y_test'''
plt.figure(0)
plt.plot(output, 'sr', label = 'output')
plt.plot(y_test, 'go', label = 'ytest')
plt.title('Accuracy')
plt.xlabel('value')
plt.ylabel('result')
plt.show()

'''tinh accuracy'''
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, output))

# confusion_matrix, precision, recall, f1score
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
cm_logistic= confusion_matrix(y_test, output)
print(cm_logistic)

precision, recall, f1score = precision_recall_fscore_support(y_test, output, average='weighted')[:3]
print("precision= {0}, recall= {1}, f1score= {2}".format(precision, recall, f1score))

'''test in test folder'''

test_value = pd.read_csv('test.csv')
X_Test = test_value[['battery_power', 'blue','clock_speed','dual_sim','fc','four_g','int_memory', 'm_dep','mobile_wt',
          'n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi']].values

pred = knn.predict(X_Test)

'''ghi vao tep test du lieu price_range'''
from pandas import DataFrame
C = {'price_range': pred}
df = DataFrame(C, columns=['price_range'])
export_csv = df.to_csv(r'result.csv', index= None, header=True)
# print(df)

test_value["price_range(banghamcosan)"] = pred

test_value.to_csv("test.csv", index=False)

# so sánh với mô hình hồi quy Logistic
import time
from sklearn.linear_model import LogisticRegression
start=time.time()
model = LogisticRegression(random_state=42).fit(x_train, y_train)
end=time.time()
print(end-start)
acc = round(model.score(x_train, y_train)*100, 2)
print(acc)
y_pred = model.predict(x_test)
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
conf = confusion_matrix(y_test, y_pred)
print(conf)
# độ chính xác, bao phủ, harmonic mean của mô hình
precision, recall, f1score = precision_recall_fscore_support(y_test, y_pred, average='weighted')[:3]
print("precision= {0}, recall= {1}, f1score= {2}".format(precision, recall, f1score))


# so sánh với mô hình DecisionTree
import time
from sklearn.tree import DecisionTreeClassifier
start=time.time()
model=DecisionTreeClassifier().fit(x_train,y_train)
end=time.time()
print(end-start)
acc = round(model.score(x_train, y_train)*100, 2)
print(acc)
y_pred = model.predict(x_test)
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
conf = confusion_matrix(y_test, y_pred)
print(conf)

precision, recall, f1score = precision_recall_fscore_support(y_test, y_pred, average='weighted')[:3]
print("precision= {0}, recall= {1}, f1score= {2}".format(precision, recall, f1score))