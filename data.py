import pandas as pd
import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost.training import train
train_set_path = "./train.csv"

train_data = pd.read_csv(train_set_path)
test_data = pd.read_csv('./test.csv')


train_x = train_data[["Pclass","Sex","Age","SibSp","Parch","Fare","Cabin","Embarked"]]
train_y = train_data[["Survived"]]
train_x = np.array(train_x)
temp = train_x[:,6]
for i in range(len(temp)):
    if temp[i] != temp[i]:
        temp[i] = 0
    else:
        temp[i] = 1
for i in range(len(train_x[:, 1])):
    if train_x[i][1] == 'male':
        train_x[i][1] = 0
    else:
        train_x[i][1] = 1
    if train_x[i][7] == 'C':
        train_x[i][7] = 1
    elif train_x[i][7] == 'S':
        train_x[i][7] = 2
    else:
        train_x[i][7] = 3

train_x[:,6] = temp
age = train_x[:,2]
train_y = np.array(train_y)
train_x, test_x, train_y, test_y = train_test_split(train_x, train_y.ravel(), test_size = 0.2, random_state = 0)
model = xgb.XGBClassifier()
model.fit(train_x, train_y.ravel(), early_stopping_rounds=100, eval_metric="auc", eval_set=[(test_x,test_y)], verbose=True)


y_pred = model.predict(test_x)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(test_y, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
model.save_model('test_1')

