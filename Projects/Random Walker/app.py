import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# -----------------------
# Random Walker Generator
# -----------------------
def random_walker(pasos):
    x = 0
    for _ in range(pasos):
        x += random.choice([-1, 1])
        yield x

# -----------------------
# UI
# -----------------------
st.title("Random Walker 1D (con yield)")
st.write("Simulación paso a paso usando generadores en Python")

pasos = st.slider("Número de pasos", 10, 500, 100)
velocidad = st.slider("Velocidad (segundos por paso)", 0.01, 0.5, 0.1)

start = st.button("Iniciar simulación")

# -----------------------
# Simulación
# -----------------------
if start:
    walker = random_walker(pasos)
    posiciones = []

    fig, ax = plt.subplots()
    line, = ax.plot([], [], marker="o")

    ax.set_xlim(0, pasos)
    ax.set_ylim(-pasos // 2, pasos // 2)
    ax.set_xlabel("Paso")
    ax.set_ylabel("Posición")

    chart = st.pyplot(fig)

    for i, pos in enumerate(walker):
        posiciones.append(pos)

        line.set_data(range(len(posiciones)), posiciones)
        ax.set_xlim(0, max(10, len(posiciones)))

        chart.pyplot(fig)
        time.sleep(velocidad)
