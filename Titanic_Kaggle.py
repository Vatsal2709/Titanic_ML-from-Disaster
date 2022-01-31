# -*- coding: utf-8 -*-
"""Titanic Kaggle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bvH4nwTI9R0Ccu8Cuji5R6XOrVZJzhri

###**Import Libraries**
"""

import pandas as pd
from sklearn import preprocessing # Label Encoding
from sklearn.linear_model import LogisticRegression # ML Model

"""### **Import Datasets**"""

data = pd.read_csv('/content/train.csv')
test = pd.read_csv('/content/test.csv')
test_id = test["PassengerId"]

data.head(5)

"""### **Data Cleaning**"""

def clean(data):
    data = data.drop(["Ticket","Cabin","Name","PassengerId"], axis=1)

    cols = ["SibSp", "Parch", "Fare", "Age"]
    for col in cols:
        data[col].fillna(data[col].mean(), inplace=True)

    data.Embarked.fillna("U", inplace=True)
    return data

   

data = clean(data)
test = clean(test)

data.head(5)

# Label Encoding
le = preprocessing.LabelEncoder()

columns = ["Sex", "Embarked"]

for col in columns:
      data[col] = le.fit_transform(data[col])
      test[col] = le.transform(test[col])
      print(le.classes_)

data.head(5)

"""### **Model Training**"""

X_train = data.drop(['Survived'], axis=1 )
Y_train = data['Survived']

lr = LogisticRegression(random_state = 0)
lr.fit(X_train, Y_train)

predicted = lr.predict(test)

r2_score = lr.score(X_train,Y_train)
print(r2_score*100,'%')

test.head()

df = pd.DataFrame({"PassengerId":test_id.values,
                   "Survived": predicted})
df.to_csv("titanic.csv", index=False)
df.head()