import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# initial state |0>
state = np.array([1, 0], dtype=complex)

# Hadamard gate
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

fig, ax = plt.subplots()

line, = ax.plot([], [], 'o')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_title("Qubit State Evolution (Hadamard)")
ax.grid()

def update(frame):
    global state

    if frame == 5:   # apply gate at step 5
        state = H @ state

    # probabilities
    p0 = np.abs(state[0])**2
    p1 = np.abs(state[1])**2

    line.set_data([p0 - p1], [0])  # simple 1D projection

    return line,

ani = FuncAnimation(fig, update, interval=500)

plt.show()