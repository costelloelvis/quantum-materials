import numpy as np

class TightBinding1D:
    def __init__(self):
        self.t = 1.0  # hopping parameter
        self.time = 0.0

    def evolve(self, dt=0.1):
        # simulate "physical evolution"
        self.time += dt
        self.t = 1.0 + 0.5 * np.sin(self.time)

    def calculate_band(self):
        k = np.linspace(-np.pi, np.pi, 200)

        # time-dependent dispersion relation
        E = -2 * self.t * np.cos(k)

        return k, E