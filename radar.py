"""
Library of useful functions for radar signal processing

author : LAHLOUH Jany
"""

import numpy as np

c = 3E8


def radarPowerBudget(Pe, Ge, Gr, sigma, lbd, L, R):
    return (Pe * Ge * Gr * sigma * lbd ** 2) / (L * (4 * np.pi) ** 3 * R ** 4)


def SNR(Pe, Ge, Gr, sigma, lbd, tho, R, L, F, K, T0):
    return (Pe * Ge * Gr * sigma * lbd ** 2 * tho) / ((4 * np.pi) ** 3 * R ** 4 * L * F * K * T0)


def SNR_N(N, Pe, Ge, Gr, sigma, lbd, tho, R, L, F, K, T0):
    return N * (Pe * Ge * Gr * sigma * lbd ** 2 * tho) / ((4 * np.pi) ** 3 * R ** 4 * L * F * K * T0)


def rangeAmbiguity(SNR_value):
    """ Range ambiguity = confusion on range measurements
    Two targets at different ranges can give the same range measurements """
    return c / (2 * 1 / SNR_value)


# Stationary target ####################################################################################################
def timeDelayStationaryTarget(R0):
    """ for one single static target"""
    return 2 * R0 / c


def distRadarStationaryTarget(T0):
    """ for one single static target"""
    return c * T0 / 2


# Moving target from range R0 with a radial velocity Vr ################################################################
def timeScaleStretching(t, Vr):
    return t * (1 + 2 * Vr / c)


def timeDelayMovingTarget(R0):
    return 2 * R0 / c


def distRadarMovingTarget(T0):
    return c * T0 / 2


def DopplerFrequency(f0, Vr):
    """ for a moving target with a radial velocity Vr"""
    return f0 * (1 + 2 * Vr / c)


def isPRFright(PRF, Vr_max, lbd):
    """ To have a proper sampling of the slow time variations (Doppler), the pulse repetition
        interval must satisfy """
    if PRF >= 2 * Vr_max / lbd:
        return True
    else:
        return False


# Antenna abilities ####################################################################################################

def antennaDirectivity(P0, Pr):
    return 4 * np.pi * P0 / Pr


def antennaGain(eta, directivity_value):
    return eta * directivity_value


def antennaGainSigma(sigma, lbd):
    return 4 * np.pi * sigma / lbd ** 2
