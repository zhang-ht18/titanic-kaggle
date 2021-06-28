import pandas as pd
import matplotlib.pyplot as plt
train_set_path = "./train.csv"

train_data = pd.read_csv(train_set_path)

women = train_data.loc[train_data.Sex == 'female']['Survived']
rate_women = sum(women) / len(women)
print('{0} women survived'.format(rate_women))

men = train_data.loc[train_data.Sex == 'male']['Survived']
rate_men = sum(men) / len(men)
print('{0} men survived'.format(rate_men))

A_class = train_data.loc[train_data.Pclass == 1]['Survived']
rate_A_class = sum(A_class) / len(A_class)
print('{0} A class survived'.format(rate_A_class))

B_class = train_data.loc[train_data.Pclass == 2]['Survived']
rate_B_class = sum(B_class) / len(B_class)
print('{0} B class survived'.format(rate_B_class))

C_class = train_data.loc[train_data.Pclass == 3]['Survived']
rate_C_class = sum(C_class) / len(C_class)
print('{0} C class survived'.format(rate_C_class))

S_destination = train_data.loc[train_data.Embarked == 'S']['Survived']
rate_S_destination = sum(S_destination) / len(S_destination)
print("{0} S destination survived".format(rate_S_destination))

C_destination = train_data.loc[train_data.Embarked == 'C']['Survived']
rate_C_destination = sum(C_destination) / len(C_destination)
print("{0} C destination survived".format(rate_C_destination))

Q_destination = train_data.loc[train_data.Embarked == 'Q']['Survived']
rate_Q_destination = sum(Q_destination) / len(Q_destination)
print("{0} Q destination survived".format(rate_Q_destination))

cabin = train_data.loc[train_data["Age"].isnull() ]['Survived']
rate_cabin = sum(cabin) / len(cabin)
print(cabin)
print("{0} with cabin survived".format(rate_cabin))





