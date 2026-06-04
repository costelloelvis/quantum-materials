import numpy as np


class DensityOfStates:

    def __init__(self, bins=200):

        self.bins = bins

    def compute(self, energies):

        dos, edges = np.histogram(
            energies,
            bins=self.bins,
            density=True
        )

        centers = (
            edges[:-1] + edges[1:]
        ) / 2

        return centers, dos