import numpy as np


def additive(odds: list) -> np.ndarray:
    n = len(odds)
    booksum = 0
    for odd in odds:
        booksum += 1/odd
    
    return np.subtract(1/np.asarray(odds), (booksum-1) / n)


def multiplicative(odds: list) -> np.ndarray:
    booksum = 0
    for odd in odds:
        booksum += 1/odd
    
    return 1 / np.multiply(odds, booksum)


def power(odds: list) -> np.ndarray:
    # helper functions for Newton-Raphson iteration
    def f(k: float) -> float:
        total = 0
        for odd in odds:
            total += (1/odd)**k
        return total - 1
    def df(k: float) -> float:
        total = 0
        for odd in odds:
            total += (1/odd)**k * np.log(1/odd)
        return total

    # initialise values
    xn = 1
    xn1 = xn - (f(xn) / df(xn))
    epsilon = 1e-8

    # repeat until convergence
    while np.abs(xn1 - xn) > epsilon:
        xn = xn1
        xn1 = xn - (f(xn) / df(xn))
    
    # return the de-vigged implied probabilities
    return np.power(odds, -xn1)