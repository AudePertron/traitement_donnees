

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#lire csv
montant = pd.read_csv('donnees//Montant_temps.csv', sep=',')

Y = montant.iloc[:,0].values

X = montant.iloc[:,1].values

#représentation graphique
plt.figure()
plt.subplot(221)
plt.plot(X,Y)

#Annotez vos courbes et amusez vous avec les paramètres d’affichages pour changer les aspects des graphiques que vous avez crées.

plt.subplot(222)
plt.plot(X,Y)
plt.ylabel('capital')
plt.xlabel('temps')
plt.title('Evolution du capital dans le temps')
plt.grid(True)
plt.annotate('à noter !', xy=(30, 20), xytext=(40, 10),
             arrowprops=dict(facecolor='orange', shrink=0.05),
             )

#nuage de points stylé
plt.subplot(223)
plt.scatter(X,Y, s = 130, c = 'yellow', marker = '*', edgecolors = 'green')




#ajuster l'espace entre les plots
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.3,
                    wspace=0.35)
plt.show()
