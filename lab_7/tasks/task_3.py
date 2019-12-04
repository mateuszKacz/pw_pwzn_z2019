import numpy as np
import random as rnd
import math


def point_range(coords):
    """Function calculates range from point (0,0) for gives point's coordinates"""

    range = math.sqrt(coords[0]**2 + coords[1]**2)

    return range


def estimate_pi(n):
    """
    Returns estimated value of pi.

    Funkcja szacuje wartość pi metodą probabilistyczną.
    Wygenerujmy m punktów z obszaru [-1,1]^2. Niech k określa liczbę punktów
    odległych od punku (0,0) o nie więcej niż 1. Proporcja 4k/m
    powinna szacować wartość pi.
    (1pkt).

    :param n: Number of points to made estimation.
    :type xy: int
    :return: Estimated Pi value
    :rtype: float
    """

    points = [[rnd.uniform(-1, 1), rnd.uniform(-1, 1)] for x in range(n)]

    calc_range = [point_range(coords) for coords in points]

    k = 0

    for calc in calc_range:

        if calc <= 1.:
            k += 1
    
    return 4*k/n


if __name__ == '__main__':
    np.testing.assert_approx_equal(estimate_pi(int(1e2)), np.pi, 1)
    np.testing.assert_approx_equal(estimate_pi(int(1e3)), np.pi, 2)

