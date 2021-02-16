import numpy as np

def ouverture(chemin):
    file = open(chemin, "r")
    file.readline()
    s = []
    for line in file:
        s.append(line)  # Ajout à la liste

    for i in range(len(s)):
        s[i] = int(s[i])  # On passe en entier
    file.close()
    signal = np.array(s)
    return signal

def load(chemin):
    contenu = np.loadtxt(chemin)
    S_emis = contenu[:, 0]
    S_recu = contenu[:, 1]
    return S_emis, S_recu

def decoupage(signal):
    print('soon')