import numpy as np
from scipy.optimize import brentq

def shin(odds: list) -> np.ndarray:
    pi = 1 / np.array(odds)
    Pi = pi.sum()
    def p_i(z, pi_i):
        num = -z + np.sqrt(z**2 + 4*(1-z)*(pi_i**2 / Pi))
        return num / (2*(1-z))
    def g(z):
        return sum(p_i(z, p) for p in pi) - 1
    try:
        z = brentq(g, 1e-5, 1 - 1e-8)
        probs = np.array([p_i(z, p) for p in pi])
        return probs
    except ValueError:
        return np.divide(pi, Pi)