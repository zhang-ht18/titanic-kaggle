import pandas as pd
#import numpy as np
train_set_path = "./train.csv"

data = pd.read_csv(train_set_path)

miss_age = data[pd.isnull(data.Age)]
class_one_miss_age = miss_age[miss_age.Pclass == 1]
print(class_one_miss_age.head(n = 30).Sex)

# feature_names = ['Age', 'Pclass']

# age_class = data[feature_names]
# miss_age_class = age_class[pd.isnull(age_class.Age)]
# age_class_map = {1:0,2:0,3:0}
# for index, row in miss_age_class.iterrows():
#     if row['Pclass'] in age_class_map:
#         age_class_map[row['Pclass']] += 1
#     else:
#         age_class_map[row['Pclass']] = 1

# print(age_class_map)




