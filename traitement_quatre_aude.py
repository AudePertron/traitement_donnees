import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import LabelEncoder

iris = pd.read_csv('C:/Users/utilisateur/Documents/microsoft_ia/traitement/iris.csv', sep=',')

#longueur_sepal
#largeur_sepal
#longueur_petal
#largeur_petal
#espèce

X=iris.iloc[:,:-1].values

Y = iris.iloc[:,-1].values

#représentation graphique
# plt.figure(1)
# plt.subplot(221)
# ax = sns.swarmplot(data=iris, x="longueur_sepal", y="largeur_sepal", hue="espèce")

# plt.subplot(222)
# ax = sns.swarmplot(data=iris, x="longueur_petal", y="largeur_petal", hue="espèce")

# plt.subplot(223)
# ax = sns.swarmplot(data=iris, x="longueur_petal", y="longueur_sepal", hue="espèce")

# plt.subplot(224)
# ax = sns.swarmplot(data=iris, x="largeur_sepal", y="largeur_petal", hue="espèce")


# plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.3,
#                     wspace=0.35)
# plt.show()


#Analyse mathématique : coefficient de corrélation de Pearson Le coefficient de corrélation linéaire simple, dit de Bravais-Pearson(ou de Pearson),
#  est une normalisation de la covariance par le produit des écarts-type des variables : rx,y = COV(X,Y) / (E(X) x E(Y)) 
# Avec les outils et bibliothèques de Python, calculez le coefficient de corrélation de Pearson sur la base de données fournie et interprétez les résultats.
x=iris.iloc[:,2:3].values


LabEnc_y = LabelEncoder()
y=LabEnc_y.fit_transform(Y)

x = np.array(x)
y = np.array(y)
y = y.reshape((y.shape[0],1))


longueur_sepal = iris.iloc[:,0].values
largeur_sepal = iris.iloc[:,1].values
longueur_petal =  iris.iloc[:,2].values
largeur_petal = iris.iloc[:,3].values


pears_long_set, p_val = stats.pearsonr(longueur_sepal, longueur_petal)

print("il semble y a avoir une corrélation assez forte entre la longeur du sepal et la longueur du pétale :" + str (pears_long_set))

print("il semble également y a avoir une corrélation assez forte entre la longeur du sepal et la largeur du pétale :" + str (stats.pearsonr(longueur_sepal, largeur_petal)))

sns.pairplot(data=iris, hue="espèce")
plt.show()