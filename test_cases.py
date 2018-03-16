import numpy as np
import matplotlib.pyplot as plt

def pulse_propagation_into_different_medium(n1, n2, freq):
    R = ((n1 - n2) / (n1 + n2)) ** 2
    T = 1 - R
    return R, T


def pulse_propagation_through_wall(n0, n1, freq, d):
    beta = 2*np.pi*freq / n1
    r01 = (n0 - n1) / (n0 + n1)
    r10 = (n1 - n0) / (n0 + n1)
    t01 = 2 * n1 / (n0 + n1)
    t10 = 2 * n0 / (n1 + n0)
    reflection_coefficient = r01 + t01 * t10 * r10 / (np.exp(1j * (2 * beta * d)) - r10 * r10)
    transmission_coefficient = t01 * t10 / (1 - r10 * r10 * np.exp(1j * (-2 * beta * d)))

    R = np.abs(reflection_coefficient) ** 2
    T = np.abs(transmission_coefficient) ** 2
    return R, T


def pulse_propagation_through_A_sandwich_radome(n0, n1, n2, beta, d1, d2):
    return None


def pulse_propagation_through_periodic_material(n1, n2, beta, d1, d2):
    return None

if __name__ == '__main__':
    # Testing propagation into a medium

    # Testing propagation through a wall
    freq = np.linspace(1, 12.56637e3, 1e3)
    n0 = 1
    n1 = 11.7
    d = 1e-3
    R, T = pulse_propagation_through_wall(n0, n1, freq, d)

    plt.plot(freq, R)
    plt.plot(freq, T)
    plt.show()
