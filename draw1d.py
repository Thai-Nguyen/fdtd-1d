import numpy as np
import matplotlib.pyplot as plt

def _test_only_vacuum():
    # Test er: only vacuum
    print('draw1d: Testing with only vacuum')
    Nz = 100
    dz = 1e-3
    E = np.ones(Nz)
    H = -np.ones(Nz)
    er = np.ones(Nz)
    draw1d(er, E, H, dz)


def _test_slab_in_vacuum():
    # Test er: slab in vacuum
    print('draw1d: Testing with slab in vacuum')
    Nz = 120
    dz = 0.01

    er_slab = 12.0
    dslab = 0.5
    nz1 = int(20)
    nz2 = int(nz1 + np.ceil(dslab/dz) - 1)

    E = np.ones(Nz)
    H = -np.ones(Nz)
    er = np.ones(Nz)
    er[nz1:nz2] = np.ones(nz2-nz1) * er_slab
    draw1d(er, E, H, dz)


def _test_periodic_structure_in_vacuum():
    # Test er: periodic structure in vacuum
    print('draw1d: Testing with periodic structure in vacuum')
    Nz = 100
    dz = 0.001

    dslab = 0.05
    nz1 = int(20)
    nz2 = int(nz1 + np.ceil(dslab/dz) - 1)

    E = np.ones(Nz)
    H = -np.ones(Nz)
    z = np.arange(0, E.size) * dz
    er = np.ones(Nz)
    er[nz1:nz2] = np.cos(2 * np.pi / 0.01 * z[nz1:nz2]) + 2
    draw1d(er, E, H, dz)


def draw1d(er, E, H, dz):
    z = np.arange(0, E.size) * dz
    for i in range(er.size - 1):
        plt.axvspan(i * dz, (i + 1) * dz, alpha=0.25, color=str(1/er[i]))
    plt.plot(z, E, 'b', z, H, 'r')

    plt.xlabel('z (m)')
    plt.legend(['E', 'H'])
    plt.show()

if __name__ == '__main__':
    _test_only_vacuum()
    _test_slab_in_vacuum()
    _test_periodic_structure_in_vacuum()