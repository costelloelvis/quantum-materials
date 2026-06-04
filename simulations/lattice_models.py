import numpy as np


class SquareLattice2D:

    def __init__(self, hopping=1.0):

        self.t = hopping

    def energy(self, kx, ky):

        return (
            -2 * self.t
            * (
                np.cos(kx)
                + np.cos(ky)
            )
        )

    def generate_band_surface(self, points=100):

        k = np.linspace(
            -np.pi,
            np.pi,
            points
        )

        KX, KY = np.meshgrid(k, k)

        E = self.energy(KX, KY)

        return KX, KY, E