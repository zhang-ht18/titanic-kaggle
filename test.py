import pandas as pd
import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost.training import train

test_data = pd.read_csv('./test.csv')

test_x = test_data[["Pclass","Sex","Age","SibSp","Parch","Fare","Cabin","Embarked"]]
passenger_id = test_data["PassengerId"]

test_x = np.array(test_x)
passenger_id = np.array(passenger_id)
passenger_id.reshape(-1,1)
print(passenger_id)
for i in range(len(test_x[:, 1])):
    if test_x[i][1] == 'male':
        test_x[i][1] = 0
    else:
        test_x[i][1] = 1
    if test_x[i][7] == 'C':
        test_x[i][7] = 1
    elif test_x[i][7] == 'S':
        test_x[i][7] = 2
    else:
        test_x[i][7] = 3
    if test_x[i][6] != test_x[i][6]:
        test_x[i][6] = 0
    else:
        test_x[i][6] = 1

model = xgb.XGBClassifier()
model.load_model('test_1')
y_pred = model.predict(test_x)
predictions = [round(value) for value in y_pred]
temp = pd.DataFrame({'PassengerId':passenger_id.tolist(), 'Survived':predictions})
temp.to_csv("ans.csv",index=False,sep=',')


