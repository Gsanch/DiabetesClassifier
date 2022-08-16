from random import random
import pandas as pd
import numpy as np
import sklearn
import shap
import io
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from matplotlib import pyplot as plt

df =pd.read_csv("test.csv")
df.dropna(subset=['Output'],inplace=True)

df['Output'].mask(df['Output'] ==0 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==1 ,'1', inplace=True)
df['Output'].mask(df['Output'] ==2 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==3 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==4 ,'1', inplace=True)
df['Output'].mask(df['Output'] ==5 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==6 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==7 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==8 ,'0', inplace=True)
df['Output'].mask(df['Output'] ==9 ,'0', inplace=True)

df.dropna(subset=['Output','Glucose','retinopathy','BMI','Blood pressure'], inplace=True)
print(df)
print(df['Output'].value_counts())
print (df.isnull().sum())
print (df)

x= df[['Glucose','retinopathy','BMI','Blood pressure','phyical health','Age']]# Features
y= df['Output'] # Labels
clf=RandomForestClassifier(n_estimators=100)
with open('trained_model', 'wb') as trained_model:
    pickle.dump(clf, trained_model)

# Split dataset into traning set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # 70% training and 30% test
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))

# explainer = shap.TreeExplainer(clf)
# shap_values = explainer.shap_values(x_test)
#   #To plot feature importance as the horizontal bar plot we need to use summary_plot method:
# shap.summary_plot(shap_values, x_test, plot_type="bar")
