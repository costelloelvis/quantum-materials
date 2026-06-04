import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------
# Quantum gates
# -------------------------
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

X = np.array([[0, 1],
              [1, 0]])

# -------------------------
# Initial state |0>
# -------------------------
state = np.array([1+0j, 0+0j])

# -------------------------
# Circuit definition (editable)
# -------------------------
circuit = ["H", "X", "H"]  # you can change this

step = 0

# -------------------------
# Visualization setup
# -------------------------
fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.set_title("Quantum Circuit Live Visualizer")
ax.set_xlabel("Amplitude difference (P0 - P1)")
ax.set_ylabel("Probability P(0)")
ax.grid()

point, = ax.plot([], [], 'bo', markersize=10)

# -------------------------
# Apply gate function
# -------------------------
def apply_gate(gate, state):
    if gate == "H":
        return H @ state
    elif gate == "X":
        return X @ state
    return state

# -------------------------
# Animation update
# -------------------------
def update(frame):
    global state, step

    # apply next gate every few frames
    if frame % 10 == 0 and step < len(circuit):
        state = apply_gate(circuit[step], state)
        step += 1

    # probabilities
    p0 = np.abs(state[0])**2
    p1 = np.abs(state[1])**2

    x = p0 - p1   # Bloch-like projection
    y = p0

    point.set_data([x], [y])

    ax.set_title(f"Step {step}/{len(circuit)} | State = {state}")

    return point,

# -------------------------
# Run animation
# -------------------------
ani = FuncAnimation(fig, update, interval=100)

plt.show()