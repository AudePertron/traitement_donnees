    #Fractionner le jeu de données pour l’entrainement et le test (Training and Test set).
    #mise à l’échelle des fonctionnalités (Feature Scaling).

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#lire csv
credit_csv = pd.read_csv('donnees/credit_immo.csv', sep=',')
#print(credit_csv)

X=credit_csv.iloc[:,-9:-1].values

imptr=SimpleImputer(missing_values=np.nan, strategy='mean')

#Adapter le model aux données
imptr.fit(X[:,0:1])
imptr.fit(X[:,7:8])

#Adapter le model aux données

X[:,0:1] = imptr.transform(X[:,0:1])
X[:,7:8] = imptr.transform(X[:,7:8])

#label encoder
LabEnc_X = LabelEncoder()
X[:,2]=LabEnc_X.fit_transform(X[:,2])
X[:,5]=LabEnc_X.fit_transform(X[:,5])

#Récupération des valeurs d'entrées et de sortie
y = credit_csv.iloc[:,-1].values
y = y.reshape((y.shape[0],1))
print(y.shape)
print(X.shape)



#Normalisation des valeurs de X
scaler = StandardScaler()
X= scaler.fit_transform(X)
print(X)

#séparation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
