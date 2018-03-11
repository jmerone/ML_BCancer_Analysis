# Python code for Breast Cancer Data

# Step 1: import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Step 2: import data and 
dataset = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
                      header = None)
# Columns indexed 1 - 9 are attributes, attribute 10 is presence of cancer
#2 for benin and 4 for malignant
#699 patients and 11 attributes 
dataset.shape()
dataset.info()
#from sklearn import 
x = dataset.iloc[:,range(1,10)].values
y = dataset.iloc[:,10].values

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.30, random_state = 1)

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

from sklearn.decomposition import PCA
pca_object = PCA(n_components = 2)
x_train = pca_object.fit_transform(x_train)
x_test = pca_object.fit_transform(x_test)
explained_variance = pca_object.explained_variance_ratio_

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

#Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
