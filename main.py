

from Detection import *
from position import *
from radar import *
from filtrage import *

if __name__ == '__main__':
    """ 1 - Pré traitement / mise en forme du signal """

    # Données d'entrée à fournir
    path = 'data/essai_reflecteur_1.txt'
    fsamp = 0
    Trec = 0
    nb_entrainement = 0
    nb_garde = 0
    taux_fa = 0

    # Ouverture de fichier
    # x = np.arange(S_recu.size)
    # fe = 9 * 10 ** 9
    # Te = 1 / fe

    # Ouverture, découpage du signal et mise sous forme de matrices

    S_emis, S_recu = load(path)
    MatrixSe = receivedSignalToMatrix(S_emis, fsamp, Trec)
    print(MatrixSe)
    MatrixSr = (S_recu, fsamp, Trec)
    print(MatrixSr)

    """ 2 - Filtrage adapté """

    MatrixSi = correlationMatrix(MatrixSe, MatrixSr)
    print(MatrixSi)

    """ 3 - Detection """

    MatrixCibles = MatrixCFAR(MatrixSi, nb_entrainement, nb_garde, taux_fa)
    print(MatrixCibles)

    """ 4 - Extraction de la localisation"""

    MatrixDistances = MatrixDistance(MatrixCibles, fsamp)
    print(MatrixDistances)

    """ 5 - Tracking """
