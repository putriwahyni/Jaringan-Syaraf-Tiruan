# -*- coding: utf-8 -*-
"""Salinan dari JST - Multi Perceptron - Kelompok

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OGzcB42NR0r7idqYPYL7-ikH0LP6bbuz
"""

import pandas as pd
from google.colab import drive

drive.mount("/content/gdrive")

# Mengambil Data
data = pd.read_excel('/content/gdrive/MyDrive/Colab Notebooks/BA_AirlineReviews_CL_excel.xlsx')
data

data.info()

print(data.isnull().sum())

"""## PreProcessing

"""

kolom_data = ['Route', 'SeatType', 'Aircraft', 'TypeOfTraveller']
data[kolom_data] = data[kolom_data].fillna(value = 'missing')
new_data = data.fillna(value =  0)
new_data

new_data = new_data.drop(columns=['id', 'ReviewHeader', 'Name', 'Datetime', 'ReviewBody', 'VerifiedReview'])
new_data

from sklearn.preprocessing import LabelEncoder

label_column = ['TypeOfTraveller']
encoder = LabelEncoder()

new_data['DateFlown'] = new_data['DateFlown'].astype('string')
new_data['Aircraft'] = new_data['Aircraft'].astype('string')

new_data['Recommended'] = new_data['Recommended'].map({'no' : 0, 'yes' : 1})

for col in ['Route', 'SeatType', 'TypeOfTraveller', 'DateFlown', 'Aircraft', 'Satisfaction'] :
    new_data[col] = encoder.fit_transform(new_data[col])

new_data

"""# Konfig Ke 1"""

# Split Data Train Test
from sklearn.model_selection import train_test_split

# Select features and target
features = new_data.loc[:, ["Satisfaction", "TypeOfTraveller", 'SeatType', 'Route', 'DateFlown']]
target = new_data.loc[:, "Recommended"]

x_train, x_test, y_train, y_test = train_test_split(features, target, train_size = 0.5, test_size = 0.5 ,random_state=50)

# Normalisasi Data
from sklearn.preprocessing import MinMaxScaler

# Feature scaling
scaler = MinMaxScaler()
scaler.fit(features)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

x_train = pd.DataFrame(x_train)
x_test = pd.DataFrame(x_test)

# Feature Engineering
from sklearn.decomposition import PCA

# apply the PCA for feature for feature reduction
pca = PCA(n_components=0.95)
pca.fit(x_train)
PCA_X_train = pca.transform(x_train)
PCA_X_test = pca.transform(x_test)

# Implementasi MLP Model

from sklearn.neural_network import MLPClassifier

# define and train an MLPClassifier named mlp on the given data
mlp = MLPClassifier(hidden_layer_sizes=(50,200,50),
      activation='relu', solver='adam', random_state=1, max_iter = 5, learning_rate_init = 0.5)
mlp.fit(PCA_X_train, y_train)

import matplotlib.pyplot as plt
import seaborn as sns

# draw the confusion matrix
predict_train = mlp.predict(PCA_X_train)
predict_test = mlp.predict(PCA_X_test)

# Implementasi Prepicion
from sklearn.metrics import precision_score, confusion_matrix, recall_score, f1_score

# Calculate precision
precision = precision_score(y_test, predict_test)
recall_score = recall_score(y_test, predict_test)
f1_score = f1_score(y_test, predict_test)

confusion_matrix = confusion_matrix(y_test, predict_test)
fig, ax = plt.subplots(1)
ax = sns.heatmap(confusion_matrix, ax=ax, cmap=plt.cm.Blues, annot=True)
plt.ylabel('True value')
plt.xlabel('Predicted value')
plt.show()

from sklearn.metrics import accuracy_score, mean_squared_error

print(f'MSE Train : {format(mean_squared_error(y_train, predict_train), ".4f")}')
print(f'Akurasi Testing : {format(accuracy_score(y_test, predict_test), ".4f")}')
print(f'Precision Testing : {format(precision, ".4f")}')
print(f'Recall Testing : {format(recall_score, ".4f")}')
print(f'F1 Score Testing : {format(f1_score, ".4f")}')

"""# Konfig 2"""

# Split Data Train Test
from sklearn.model_selection import train_test_split

# Select features and target
features = new_data.loc[:, ["Satisfaction", "TypeOfTraveller", 'SeatType', 'Route','DateFlown']]
target = new_data.loc[:, "Recommended"]

x_train, x_test, y_train, y_test = train_test_split(features, target, train_size = 0.7, test_size = 0.3 ,random_state=50)

# Normalisasi Data
from sklearn.preprocessing import MinMaxScaler

# Feature scaling
scaler = MinMaxScaler()
scaler.fit(features)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

x_train = pd.DataFrame(x_train)
x_test = pd.DataFrame(x_test)

# Feature Engineering
from sklearn.decomposition import PCA

# apply the PCA for feature for feature reduction
pca = PCA(n_components=0.95)
pca.fit(x_train)
PCA_X_train = pca.transform(x_train)
PCA_X_test = pca.transform(x_test)

# Implementasi MLP Model

from sklearn.neural_network import MLPClassifier

# define and train an MLPClassifier named mlp on the given data
mlp = MLPClassifier(hidden_layer_sizes=(50,200,50),
      activation='relu', solver='adam', random_state=1, max_iter = 10, learning_rate_init = 0.05)
mlp.fit(PCA_X_train, y_train)

import matplotlib.pyplot as plt
import seaborn as sns

# draw the confusion matrix
predict_train = mlp.predict(PCA_X_train)
predict_test = mlp.predict(PCA_X_test)

# Implementasi Precision, matrix, recall, f1
from sklearn.metrics import precision_score, confusion_matrix, recall_score, f1_score

# Calculate precision
precision = precision_score(y_test, predict_test)
recall_score = recall_score(y_test, predict_test)
f1_score = f1_score(y_test, predict_test)

confusion_matrix = confusion_matrix(y_test, predict_test)
fig, ax = plt.subplots(1)
ax = sns.heatmap(confusion_matrix, ax=ax, cmap=plt.cm.Blues, annot=True)
plt.ylabel('True value')
plt.xlabel('Predicted value')
plt.show()

from sklearn.metrics import accuracy_score, mean_squared_error

print(f'MSE Train : {format(mean_squared_error(y_train, predict_train), ".4f")}')
print(f'Akurasi Testing : {format(accuracy_score(y_test, predict_test), ".4f")}')
print(f'Precision Testing : {format(precision, ".4f")}')
print(f'Recall Testing : {format(recall_score, ".4f")}')
print(f'F1 Score Testing : {format(f1_score, ".4f")}')

"""# Konfig 3"""

# Split Data Train Test
from sklearn.model_selection import train_test_split

# Select features and target
features = new_data.loc[:, ["Satisfaction", "TypeOfTraveller", 'SeatType', 'Route']]
target = new_data.loc[:, "Recommended"]

x_train, x_test, y_train, y_test = train_test_split(features, target, train_size = 0.9, test_size = 0.1 ,random_state=50)

# Normalisasi Data
from sklearn.preprocessing import MinMaxScaler

# Feature scaling
scaler = MinMaxScaler()
scaler.fit(features)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

x_train = pd.DataFrame(x_train)
x_test = pd.DataFrame(x_test)

# Feature Engineering
from sklearn.decomposition import PCA

# apply the PCA for feature for feature reduction
pca = PCA(n_components=0.95)
pca.fit(x_train)
PCA_X_train = pca.transform(x_train)
PCA_X_test = pca.transform(x_test)

# Implementasi MLP Model

from sklearn.neural_network import MLPClassifier

# define and train an MLPClassifier named mlp on the given data
mlp = MLPClassifier(hidden_layer_sizes=(25,100,25), activation='relu', solver='adam', random_state=1, max_iter = 5, learning_rate_init = 0.5)
mlp.fit(PCA_X_train, y_train)

import matplotlib.pyplot as plt
import seaborn as sns

# draw the confusion matrix
predict_train = mlp.predict(PCA_X_train)
predict_test = mlp.predict(PCA_X_test)

# Implementasi Prepicion
from sklearn.metrics import precision_score, confusion_matrix, recall_score, f1_score

# Calculate precision
precision = precision_score(y_test, predict_test)
recall_score = recall_score(y_test, predict_test)
f1_score = f1_score(y_test, predict_test)

confusion_matrix = confusion_matrix(y_test, predict_test)
fig, ax = plt.subplots(1)
ax = sns.heatmap(confusion_matrix, ax=ax, cmap=plt.cm.Blues, annot=True)
plt.ylabel('True value')
plt.xlabel('Predicted value')
plt.show()

from sklearn.metrics import accuracy_score, mean_squared_error

print(f'MSE Train : {format(mean_squared_error(y_train, predict_train), ".4f")}')
print(f'Akurasi Testing : {format(accuracy_score(y_test, predict_test), ".4f")}')
print(f'Precision Testing : {format(precision, ".4f")}')
print(f'Recall Testing : {format(recall_score, ".4f")}')
print(f'F1 Score Testing : {format(f1_score, ".4f")}')