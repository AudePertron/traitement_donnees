import pandas as pd
import numpy as np

#Mesure de tendance centrale est le nombre qui caractérise le centre d’une distribution et la position des diverses valeurs de la distribution par rapport à ce centre. 
# Il s’agit ici de calculer la moyenne, le médiane et le mode d’une distribution. Vous avez à disposition le fichier nommé tendance_centrale.csv. 
# Chargez ces données puis en utilisant les outils nécessaires appliquez la mesure de tendance centrale sur ces données.

#lire csv
tendance = pd.read_csv('C:/Users/utilisateur/Documents/microsoft_ia/traitement/tendance_centrale.csv', sep=',')

#moyenne
#age_mean = tendance.Age.mean()
#print("moyenne d'age : " + str(age_mean))

#rating_mean = tendance.Rating.mean()
#print("note moyenne : " + str(rating_mean))

moyenne = tendance[['Age', 'Rating']].mean()
print("moyenne ", str(moyenne) )
#médiane
#age_median = tendance.Age.median()
#print("age médian : " + str(age_median))

#rating_median = tendance.Rating.median()
#print("note médianne: " + str(rating_median))
median = tendance[['Age', 'Rating']].median()

#mode
#age_mode = tendance.Age.mode()
#print("age plus fréquent : " + str(age_mode))

#rating_mode = tendance.Rating.mode()
#print("note plus fréquente: " + str(rating_mode))
mode = tendance[['Age', 'Rating']].mode()

#Faites une analyse de variance sur le jeu de données issu de tendance_centrale.csv

variance = tendance[['Age', 'Rating']].var()

