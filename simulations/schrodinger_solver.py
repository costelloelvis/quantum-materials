import numpy as np
from scipy.linalg import eigh


class SchrodingerSolver:

    def __init__(self, xmin=-5, xmax=5, npoints=1000):

        self.x = np.linspace(xmin, xmax, npoints)
        self.dx = self.x[1] - self.x[0]

    def solve(self, potential):

        N = len(self.x)

        kinetic = (
            -0.5
            * (
                np.diag(np.ones(N - 1), -1)
                - 2 * np.diag(np.ones(N), 0)
                + np.diag(np.ones(N - 1), 1)
            )
            / self.dx**2
        )

        H = kinetic + np.diag(potential)

        energies, states = eigh(H)

        return energies, states


def harmonic_potential(x):
    return 0.5 * x**2


if __name__ == "__main__":

    solver = SchrodingerSolver()

    V = harmonic_potential(solver.x)

    E, psi = solver.solve(V)

    print("Lowest 5 energy levels")

    for i in range(5):
        print(i, E[i])