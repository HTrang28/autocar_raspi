import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#xay dung ham tinh toan(A va B la 2 diem, n la so luong dac tinh
def caclDistances( A, B, n = 20):
    temp = 0
    for i in range(n):
        temp += (float(A[i]) - float(B[i]))**2
    temp = math.sqrt(temp)
    return temp

#xay dung ham tim k diem gan nhat
def KNNeighbor(data_train , point, k) :
    distance = []
    for item in data_train :
        distance.append({
            "label": item[-1],
            "value":caclDistances(item, point)
        })
    distance.sort(key=lambda x: x["value"])
    labels = [item["label"] for item in distance]
    return labels[:k]

#xay dung ham tim dien thoai xuat hien nhieu nhat trong k lan
def FindKNN (arr) :
    labels = set(arr) #truyen arr vao labels
    max_mobile = -1
    for label in labels:
        mobile = arr.count(label) #tra ve so luong phan tu co gia tri la label nhieu nhat trong arr
        if mobile > max_mobile :
            max_mobile = mobile
            res = label
    return res

# doc data train tu file
train = pd.read_csv('train.csv')

X = train[['battery_power', 'blue','clock_speed','dual_sim','fc','four_g','int_memory', 'm_dep','mobile_wt',
          'n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi','price_range']].values
Y = train[['price_range']].values

# X = np.array(list(X))
# print(X[0][0])

#Chia tep train de thuc hien train
p = np.random.permutation(len(X)) #tron data
x_train = X[p[:int(0.8*len(X))]].copy()
x_test  = X[p[int(0.8*len(X)):]].copy()
# print(x_train[0][0],'   ',x_train[0][1],'\n',x_train[1][0],'      ',x_train[1][1],'  ',x_train[1][2])
# y_train = Y[p[:int(0.8*len(X))]].copy()
y_test  = Y[p[int(0.8*len(X)):]].copy()

#duyet cac du lieu trong bo test de kiem tra
count = 0
ansTrain =[]
for item in x_test:
    knn = KNNeighbor(x_train, item, 11)
    result = FindKNN(knn)
    # print("label: {} -> pred: {}".format(item[-1],result))
    ansTrain.append(result)
    if item[-1] != result :
        count += 1
#show ket qua bang do thi
plt.figure(0)
plt.plot(ansTrain, 'sr', label = 'result')
plt.plot(y_test, 'go', label = 'ytest')
plt.title('Accuracy')
plt.xlabel('value')
plt.ylabel('result')
plt.show()


# tính accuracy
from sklearn.metrics import accuracy_score
E = accuracy_score(y_test, ansTrain)
print(' Accuracy : ', E)
print('So phep sai : {0}; accuracy: {1}'.format(count, (400-count)/400))

## confusion_matrix, precision, recall, f1score
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
cm_logistic= confusion_matrix(y_test, ansTrain)
print(cm_logistic)

precision, recall, f1score = precision_recall_fscore_support(y_test, ansTrain, average='weighted')[:3]
print("precision= {0}, recall= {1}, f1score= {2}".format(precision, recall, f1score))

#Test bang bo test
test = pd.read_csv('test.csv')
X_Test = test[['battery_power', 'blue','clock_speed','dual_sim','fc','four_g','int_memory', 'm_dep','mobile_wt',
          'n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi']].values

ansTest = []
for item in X_Test:
    knn = KNNeighbor(x_train, item, 11)
    result = FindKNN(knn)
    ansTest.append(result)

# luu file
test['price_range(tuxdmodel)'] = ansTest
test.to_csv('test.csv',  index=False)

print('process has finish')

#so sanh voi ket qua train tu cac ham co san
result_func_exist = test['price_range(banghamcosan)'].values
result_func_notexist = test['price_range(tuxdmodel)'].values

error = 0
for i in range(len(result_func_exist)):
    if result_func_exist[i] != result_func_notexist[i]:
        error += 1
print('error : ', error )