import numpy as np
import math as m
import matplotlib.pyplot as plt

"""on fait de la dimension 1. Utilisation de l'axe des x"""


def distance_eucl(donnee, d):
    """donnée : [y] (pas de prise en compte des x) c'est la distance au radar placé en 0 et d : liste de data de la forme [y, classe], data étant une liste de listes des données déjà traitées et disponibles
    renvoit pour chaque point du set de donnée la distance au nouveau plot en position y selon
    distance < 0 : le point est plus loin sur l'axe
    distance > 0 : le point est plus proche"""
    distance = 0.0
    distance = distance + (donnee[0] - d[0])
    return distance


def trouver_voisins(data, donnee, nb_voisins):
    """data: liste : ensemble de donnee à tester, d in data est de la forme [y,piste]
    donnee est la donnée testée de la forme [y]
    nb_voisins = k = nb de voisins souhaités
    on gère aussi la création d'une nouvelle piste si les distance aux k plus proches voisins sont trop grandes """
    distances = []
    for d in data:
        dist = distance_eucl(donnee, d)
        distances.append((d, dist))
    # tri
    distances.sort(key=lambda tup: tup[1])
    voisins = []

    # vérification distances
    seuil = 2
    cpt = 0
    for i in range(nb_voisins):
        if np.abs(distances[i][1]) > seuil:
            cpt += 1
    if cpt == nb_voisins:
        print("le plot n'appartient à aucune piste, on en crée une nouvelle")
    else:
        for i in range(nb_voisins):
            voisins.append(distances[i][0])

    # création listes des k plus proches voisins : à décommenter si on ne fait pas la vérification de distances
    # for i in range(nb_voisins):
    # voisins.append(distances[i][0])

    # on renvoit les k plus proches voisins de la donnée testée
    print("voisins:", voisins)
    return voisins


def prediction_classe(data, donnee, nb_voisins):
    """data: liste : ensemble de donnee à tester, d in data est de la forme [y,piste]
        donnee est la donnée testée de la forme [y]
        nb_voisins = k = nb de voisins souhaités"""
    voisins = trouver_voisins(data, donnee, nb_voisins)
    if not voisins:
        print("nouvelle affectation")
        prediction = 100
    else:
        output = [d[-1] for d in voisins]
        prediction = max(set(output), key=output.count)

    return prediction


def ajout(data, donnee, classe_donnee):
    """on ajoute la donnée à la bonne piste"""
    donnee.append(classe_donnee)
    data.append(donnee)
    return data


def suivi_1_cible(donnee, piste, k):
    """on se donne en entrée la donnée à tester. On ne suit qu'une seule cible. il faut mettre en place une
    discrimination pour pouvoir créer une nouvelle piste si un plot est loin par rapport à un seuil déterminé il faut
    aussi pouvoir dropper cette piste si on ne détecte pas d'autre plots autour de ce dernier dans les 3 prochaines
    acquisitions """
    # data = []
    radar = [0]  # position de l'observateur

    # visualisation
    plt.figure()
    plt.subplot(211)
    plt.plot(piste[0][0], 'bo', color='blue', label="piste")
    for i in range(1, len(piste)):
        plt.plot(piste[i - 1][0], color='blue')
        plt.plot(piste[i][0], 'bo', color='blue')

    plt.plot(donnee[0], 'bo', color="green", label="plot à tester")
    plt.plot(radar[0], 'bo', color="yellow", label="radar")
    plt.legend()
    plt.grid()
    plt.xlabel("abs")
    plt.ylabel("ordonnées")
    plt.title("situation N")
    # fin visualisation

    # prediction
    classe_donnee = prediction_classe(piste, donnee, k)

    # nouvelle piste au cas ou on en ait besion
    piste_nvx = []

    if classe_donnee != 100:
        print("le plot appartient à la piste")
        donnee.append(classe_donnee)
        piste.append(donnee)
        distance_cible_radar = distance_eucl(donnee, radar)
        distance_donne_precedent = distance_eucl(donnee, piste[-2])

        print("piste mise à jour:", piste)
        print("le nouveau point est à :", distance_cible_radar, "m du radar")
        print("le point c'est déplacé de:", distance_donne_precedent,
              "m entre son emplacement précédent et son emplacement actuel")

        # visualisation
        plt.subplot(212)
        plt.plot(piste[0][0], 'bo', color='blue', label="piste")
        for i in range(1, len(piste)):
            plt.plot(piste[i - 1][0], color='blue')
            plt.plot(piste[i][0], 'bo', color='blue')
        plt.plot(radar[0], 'bo', color="yellow", label="radar")
        plt.legend()
        plt.grid()
        plt.xlabel("abs")
        plt.ylabel("ordonnées")
        plt.title("situation N+1")

    else:
        # on traite les cas divergents ici
        # on crée la nouvelle piste, on oublie pas de gérer un eventuel drop.
        print("le plot n'appartient pas à la piste")
        donnee.append(34)
        print("la nouvelle piste associée porte le numéro 34")
        piste_nvx.append(donnee)
        distance_donne_precedent = 0
        distance_cible_radar = distance_eucl(donnee, radar)

        print("nouvelle piste:", piste_nvx, "\n piste :", piste)
        print("le nouveau point est à :", distance_cible_radar, "m du radar")


        # visualisation
        plt.subplot(212)
        plt.plot(piste[0][0], 'bo', color='blue', label="piste")
        plt.plot(piste_nvx[0][0], 'bo', color='red', label="nouvelle piste")
        for i in range(1, len(piste)):
            plt.plot(piste[i - 1][0], color='blue')
            plt.plot(piste[i][0], 'bo', color='blue')
        plt.plot(radar[0], 'bo', color="yellow", label="radar")
        plt.legend()
        plt.grid()
        plt.xlabel("abs")
        plt.ylabel("ordonnées")
        plt.title("situation N+1")

    return piste, piste_nvx, distance_donne_precedent
    plt.show()

if __name__ == "__main__":
    donnee = [4]
    donnee_eclatee_au_sol = [20]
    k = 3  # nombre de voisins souhaité

    # on suppose que les pistes sont "triées" dans l'ordre d'apparition des plots dans cette dernière
    piste_1 = [[7, 1],
               [8, 1],
               [1, 1],
               [-2, 1],
               [2, 1]
               ]
    piste_2 = [[2, 2],
               [4, 2],
               [6, 2],
               [7, 2],
               [8, 2]]

    piste_3 = [[0.5, 3],
               [1, 3],
               [1.5, 3],
               [3, 3],
               [4, 3]]

    piste_1, piste_nvx, distance = suivi_1_cible(donnee_eclatee_au_sol, piste_1, 3)
    piste_1, piste_nvx, distance = suivi_1_cible(donnee, piste_1, 3)
    print(piste_1)
    #print(piste_nvx) :  ne marche pas car écrasé par le deuxième appel de suivi_1_cible -> il faut passer sur un suivi de 2 cibles (if piste_nvx != [] : suivi_2_cible else : on enchaine 
