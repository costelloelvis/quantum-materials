import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parents[1]
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulations.band_structure import TightBinding1D


def run_live_band():
    model = TightBinding1D()

    fig, ax = plt.subplots()
    line, = ax.plot([], [])

    ax.set_xlim(-3.14, 3.14)
    ax.set_ylim(-3, 3)
    ax.set_title("LIVE Quantum Band Evolution")
    ax.set_xlabel("k")
    ax.set_ylabel("Energy")
    ax.grid()

    def update(frame):
        model.evolve(dt=0.1)   # 🔥 THIS is the key change

        k, E = model.calculate_band()
        line.set_data(k, E)

        return line,

    ani = FuncAnimation(fig, update, interval=100, blit=True)

    plt.show()


if __name__ == "__main__":
    run_live_band()