from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def intercorrelation(s,r):
    i=signal.correlate(s,r)
    lags = signal.correlation_lags(len(s), len(r))
    i/=np.max(i)
    fig, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1)
    ax_corr.plot(-lags,i)
    ax_orig.plot(s)
    ax_noise.plot(r)
    plt.show()


def correlationMatrix(Me, Mr):
    """
    param :
        - Me : pulses Matrix
        - Mr : listening time Matrix
    output : correlation Matrix
    """
    N, M = np.shape(Mr)
    s = Me.tolist()
    r = Mr.tolist()
    l = []
    for i in range(M):
        l.append(signal.correlate(s[i], r[i]))
    Ml = np.asarray(l)
    return Ml





