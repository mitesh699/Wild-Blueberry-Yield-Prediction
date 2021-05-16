import numpy as np
import csv
import pandas as pd
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("BlueberryDataset.csv")
dataset = dataset.drop(columns='Row#')

X = dataset.drop(columns=['yield'])
y = dataset['yield']

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

rf.fit(X_train, Y_train)

print(rf.predict(X_test))

import joblib
joblib.dump(rf, 'randomforest.joblib')

print(X_test.head())