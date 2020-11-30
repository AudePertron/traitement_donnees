import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as mp
import json

#lire csv
credit_csv = pd.read_csv('C:/Users/utilisateur/Documents/microsoft_ia/traitement/credit_immo.csv', sep=',')
print(credit_csv.head())

#lire json
with open('C:/Users/utilisateur/Documents/microsoft_ia/traitement/credit_immo.json') as json_data:
    credit_json = json.load(json_data)
    print(credit_json)

#lire xls
df = pd.read_excel
credit_xls = pd.read_excel('C:/Users/utilisateur/Documents/microsoft_ia/traitement/credit_immo.xls')
print(credit_xls.head())


# En utilisant les bibliothèques adéquates, créer une base de données formée de 6 lignes et 4 colonnes. 
#Les colonnes représentent respectivement les variables "taux_de_ventes, croissance_vente, ratio_benefice, ratio_perte".

column_names = ["taux_de_ventes", "croissance_vente", "ratio_benefice", "ratio_perte"]
index_data = [1,2,3,4,5,6]
data_test = pd.DataFrame(columns = column_names, index= index_data)
print(data_test)

#En utilisant la fonction dataset.reindex() et dataset.isnull(), introduire des données manquantes et récupérer les indices des valeurs manquantes.
# Puis remplacez les valeurs manquantes par 0 par exemple. Puis supprimez ces valeurs manquantes.

print(data_test.isnull)


new_index =["nb_ventes", "augmentation", "diminution", "chiffre_affaire"]
print(data_test.reindex(new_index, fill_value=0))

