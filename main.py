
import numpy as np
from Detection import *
from position import *
from radar import *
from filtrage import *

if __name__ == '__main__':
    """ 1 - Pré traitement / mise en forme du signal """

    # Données d'entrée à fournir
    path = 'data/chirp_perso.txt'
    fsamp = 1500e6
    Trec = 260e-6
    nb_entrainement = 100
    nb_garde = 25
    taux_fa = 1e-6

    # Ouverture de fichier
    # x = np.arange(S_recu.size)
    # fe = 9 * 10 ** 9
    # Te = 1 / fe

    # Ouverture, découpage du signal et mise sous forme de matrices

    S_emis, S_recu = load(path)
    #print(type(S_emis))
    MatrixSe = receivedSignalToMatrix(S_emis, fsamp, Trec)
    #print(MatrixSe)
    MatrixSr = receivedSignalToMatrix(S_recu, fsamp, Trec)
    #(MatrixSr)

    """ 2 - Filtrage adapté """

    MatrixSi = correlationMatrix(MatrixSe, MatrixSr)
#print(MatrixSi)


    """ 3 - Detection """

    MatrixCibles = MatrixCFAR(MatrixSi, nb_entrainement, nb_garde, taux_fa)
    #print(MatrixCibles)
    plot_Cibles(list(range(len(MatrixSi[0].tolist()))), MatrixSi[0].tolist(), MatrixCibles[0].tolist())

    """ 4 - Extraction de la localisation"""

    MatrixDistances = MatrixDistance(MatrixCibles, fsamp)
    print(MatrixDistances)

    """ 5 - Tracking """
