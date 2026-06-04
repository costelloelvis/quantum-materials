import sys
from pathlib import Path

# Safeguard pathing for Streamlit execution context
root_dir = Path(__file__).resolve().parents[1]
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import streamlit as st
import matplotlib.pyplot as plt
from simulations.band_structure import TightBinding1D
from simulations.density_of_states import DensityOfStates

st.set_page_config(page_title="Quantum Materials Discovery", layout="wide")
st.title("Quantum Materials Discovery Platform")

st.sidebar.header("Simulation Parameters")
t = st.sidebar.slider("Hopping Parameter", 0.1, 5.0, 1.0)

model = TightBinding1D(hopping=t)
k, E = model.calculate_band()

fig1, ax1 = plt.subplots()
ax1.plot(k, E)
ax1.set_title("Band Structure")
ax1.set_xlabel("k")
ax1.set_ylabel("Energy")
st.pyplot(fig1)

dos_calc = DensityOfStates()
energy, dos = dos_calc.compute(E)

fig2, ax2 = plt.subplots()
ax2.plot(energy, dos)
ax2.set_title("Density of States")
ax2.set_xlabel("Energy")
ax2.set_ylabel("DOS")
st.pyplot(fig2)