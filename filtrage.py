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