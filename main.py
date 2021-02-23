import numpy as np



from filtrage import intercorrelation
from Detection import CFAR, plot_Cibles
from position import distance
from radar import *


if __name__ == '__main__':


    """ 1 - Pré traitement / mise en forme du signal """
    # Ouverture de fichier
    signal = ouverture("data/test1.txt")
    S_emis, S_recu = load('data/acquisition.txt')
    x = np.arange(S_recu.size)
    fe = 15 * 10 ** 9
    Te = 1 / fe
    # Découpage du signal
0


""" 2 - Filtrage adapté """
intercorrelation(S_emis[4800:6300], S_recu[4800:6300])


""" 3 - Detection """
idx_pics = CFAR(signal, 100, 10, 0.26)
plot_Cibles(x, signal, idx_pics)

""" 4 - Extraction de la localisation"""
distance(fe, idx_pics)


""" 5 - Tracking """






