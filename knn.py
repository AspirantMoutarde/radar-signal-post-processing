# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:14:32 2020

@author: emili
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

"""algorithme des k plus proches voisins pour la prédiction de la prochaine position de la cible.
tracking
ce fait en 3 étapes :
    - calcul de la distance aux autres points : ici distance euclidienne
    - identifier les plus proches voisins
    - prédiction"""

"""calcul de la distance euclidienne
on met les données à tester sous la forme : data = [[x0,y0,classe],[x1,y1, classe],...]
classe représente la piste à laquelle appartient la donnée (1 piste = 1 classe)
On renvoit "distance" : plus cette valeur est petite, plus les données sont similaires
on pose donnee = data[0]
on boucle :
    for d in data :
        distance = distance_eucl(donnee,d)"""



def distance_eucl(donnee, d):
    """donnée du type liste [x,y] et data du type liste [x, y, classe]"""
    distance = 0.0
    distance = distance + (d[0] - donnee[0]) ** 2 + (d[1] - donnee[1]) ** 2
    return m.sqrt(distance)


"""on a donc calculé la distance du nouveau point aux autres points déjà relevé
on détermine les k plus proches voisins du nouveau point data[0] à l'aide d'un fonction de tri
trouver_voisins(data,data[0],k)"""


def trouver_voisins(data, donnee, nb_voisins):
    """data: liste : ensemble de donnee à tester, d in data est de la forme [x,,y,piste]
    donnee est la donnée testée de la forme [x, y]
    nb_voisins = k = nb de voisins souhaités"""
    distances = []
    for d in data:
        dist = distance_eucl(donnee, d)
        distances.append((d, dist))
    # tri
    distances.sort(key=lambda tup: tup[1])
    voisins = []
    for i in range(nb_voisins):
        voisins.append(distances[i][0])

    # on renvoit les k plus proches voisins de la donnée testée
    return voisins


"""prédiction à effectuer : on fonctionne avec des classes
Une classe = une piste ie trajectoire
On cherche à quelle classe ajouter le nouveau points data[0]"""


def prediction_classe(data, donnee, nb_voisins):
    voisins = trouver_voisins(data, donnee, nb_voisins)
    output = [d[-1] for d in voisins]
    prediction = max(set(output), key=output.count)
    return prediction


def ajout(data, donnee, classe_donnee):
    """on ajoute la donnée à la bonne piste"""
    donnee.append(classe_donnee)
    data.append(donnee)
    return data


# test des 4 fonctions avec jeu de données
if __name__ == "__main__":

    donnee = [5, 5]

    data = [[7, 7, 1],
            [8, 7, 1],
            [2, 1.8, 2],
            [1, 2, 1],
            [-2, 2, 1],
            [6, 5, 2],
            [8, 6, 2],
            [2, 2, 1],
            [6, 6.4, 2],
            [0, 3, 2]
            ]


    plt.figure()
    plt.subplot(121)
    for d in data:
        if d[2] == 1:
            plt.plot(d[0], d[1], 'bo', color="green")
        else:
            plt.plot(d[0], d[1], 'bo')
    plt.plot(donnee[0], donnee[1], 'bo', color="red", label="pt à tester")

    plt.legend()
    plt.grid()
    plt.xlabel("abs")
    plt.ylabel("ordonnées")
    plt.title("situation de départ")

    classe_donnee = prediction_classe(data, donnee, 3)
    print(classe_donnee)

    data = ajout(data, donnee, classe_donnee)
    print(data)

    plt.subplot(122)
    for d in data:
        if d[2] == 1:
            plt.plot(d[0], d[1], 'bo', color="green")
        else:
            plt.plot(d[0], d[1], 'bo')

    plt.grid()
    plt.xlabel("abs")
    plt.ylabel("ordonnées")
    plt.title("après algo knn")

    plt.show()
