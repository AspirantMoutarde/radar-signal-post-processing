import numpy as np



from filtrage import intercorrelation
from Detection import CFAR, plot_Cibles
from position import distance
from radar import *
from affichage import *

if __name__ == '__main__':

    """ 1 - Pré traitement / mise en forme du signal """
    # Ouverture de fichier
    #signal = ouverture("data/essai_reflecteur_1.txt")
    S_emis, S_recu = load('data/essai_reflecteur_1.txt')
    print(S_emis,S_recu)
    x = np.arange(S_recu.size)
    fe = 9 * 10 ** 9
    Te = 1 / fe
    # Découpage du signal


    """ 2 - Filtrage adapté """
    intercorrelation(S_emis, S_recu)

    """ 3 - Detection """
    #idx_pics = CFAR(signal, 100, 10, 0.26)
    #plot_Cibles(x, signal, idx_pics)

    """ 4 - Extraction de la localisation"""
    #distance(fe, idx_pics)


    """ 5 - Tracking """






