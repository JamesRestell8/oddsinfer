import numpy as np


def brier(probs: list, outcome_index: int) -> float:
    sum_sq = np.sum(np.square(probs))
    q_y = probs[outcome_index]
    return sum_sq - 2 * q_y + 1


def log_loss(probs: list, outcome_index: int) -> float:
    winner = probs[outcome_index]
    return -np.log(winner)