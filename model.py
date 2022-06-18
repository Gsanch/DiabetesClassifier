import pandas as pd
import numpy as np
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

df =pd.read_csv("test.csv")
df.dropna(subset=['Output'],inplace=True)
print (df.isnull().sum())

df['Output'].mask(df['Output'] ==0,'1', inplace=True)
df['Output'].mask(df['Output'] ==1,'0', inplace=True)
df['Output'].mask(df['Output'] ==2 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==3 ,'1', inplace=True)
df['Output'].mask(df['Output'] ==4 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==5 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==6 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==7 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==8 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==9 ,'0', inplace=True)

df.dropna(subset=['Output','Glucose','retinopathy','BMI','Blood pressure'], inplace=True)
print(df)
print(df['Output'].value_counts())

x= df[['Glucose','retinopathy','BMI','Blood pressure','phyical health','Age']] # Features
y= df['Output'] # Labels
clf=RandomForestClassifier(n_estimators=100)
# Split dataset into traning set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # 70% training and 30% test
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
