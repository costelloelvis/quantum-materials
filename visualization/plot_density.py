import sys
from pathlib import Path

# Insert project root directory into python path
root_dir = Path(__file__).resolve().parents[1]
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import matplotlib.pyplot as plt
from simulations.band_structure import TightBinding1D
from simulations.density_of_states import DensityOfStates


def plot_dos():
    model = TightBinding1D()
    k, E = model.calculate_band(points=100000)

    dos_calc = DensityOfStates()
    energy, dos = dos_calc.compute(E)

    plt.figure(figsize=(8, 5))
    plt.plot(energy, dos)
    plt.title("Density of States")
    plt.xlabel("Energy")
    plt.ylabel("DOS")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    plot_dos()