"""
Extarction de distances, position etc...
@author: Janyl
"""
def distance(frec, cibles):
    """
    Détermination des distances cibles - radar
    :param frec: frequence d'échantillonnage
    :param cibles: liste des cibles détectées (indices dans la listes du signal reçu)
    :return: distanbances de chaque cible au radar en mètres
    """
    c = 3E8
    Distances = []
    for i in cibles:
        T = 1 / frec  # Période d'échantillonage
        Dt = cibles[i] = T  # Décallage temporel de l'écho due à la cible
        R = (c * abs(Dt)) / 2  # Distance cible - radar
        Distances.append(R)

    return Distances


def coordonnees():
    print('soon')
