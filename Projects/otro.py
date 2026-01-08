import streamlit as st
import random
import time
import matplotlib.pyplot as plt
# -----------------------
# Walker Class 1D
# -----------------------
class Walker1D:
    def __init__(self, x=0):
        self.x = x
        self.posiciones = [x]
    
    def walk(self, pasos):
        """Generador que produce pasos en 1D"""
        for _ in range(pasos):
            flip = random.choice(["Heads", "Tails"])
            
            if flip == "Heads":
                self.x += 1  # Step right
            else:
                self.x -= 1  # Step left
            
            self.posiciones.append(self.x)
            yield self.x
    
    def draw(self, ax):
        """Dibuja el camino en 1D"""
        if len(self.posiciones) > 0:
            ax.plot(range(len(self.posiciones)), self.posiciones, marker="o", linestyle="-", markersize=6)
            ax.plot(len(self.posiciones) - 1, self.posiciones[-1], marker="o", color="red", markersize=10)

# -----------------------
# Walker Class 2D
# -----------------------
class Walker2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.posiciones = [(x, y)]
    
    def walk(self, pasos):
        """Generador que produce pasos basados en lanzamientos de moneda"""
        for _ in range(pasos):
            flip1 = random.choice(["Heads", "Tails"])
            flip2 = random.choice(["Heads", "Tails"])
            
            if flip1 == "Heads" and flip2 == "Heads":
                self.y += 1  # Step forward
            elif flip1 == "Heads" and flip2 == "Tails":
                self.x += 1  # Step right
            elif flip1 == "Tails" and flip2 == "Heads":
                self.x -= 1  # Step left
            else:  # Tails and Tails
                self.y -= 1  # Step backward
            
            self.posiciones.append((self.x, self.y))
            yield (self.x, self.y)
    
    def draw(self, ax):
        """Dibuja el camino recorrido en el plano"""
        if len(self.posiciones) > 0:
            xs, ys = zip(*self.posiciones)
            ax.plot(xs, ys, marker="o", linestyle="-", markersize=6)
            ax.plot(xs[-1], ys[-1], marker="o", color="red", markersize=10)

# -----------------------
# UI
# -----------------------
st.title("Random Walker Simulator")
st.write("Simulación de caminantes aleatorios en 1D y 2D")

# Crear pestañas
tab1, tab2 = st.tabs(["Random Walker 1D", "Random Walker 2D"])

# -----------------------
# PESTAÑA 1D
# -----------------------
with tab1:
    st.header("Random Walker Lineal (1D)")
    st.write("Movimiento en línea recta: Heads = derecha, Tails = izquierda")
    
    pasos_1d = st.slider("Número de pasos", 10, 500, 100, key="slider_1d")
    velocidad_1d = st.slider("Velocidad (segundos por paso)", 0.01, 0.5, 0.1, key="slider_vel_1d")
    
    start_1d = st.button("Iniciar simulación 1D", key="btn_1d")
    
    if start_1d:
        walker_1d = Walker1D()
        
        fig, ax = plt.subplots(figsize=(10, 5))
        chart_placeholder = st.pyplot(fig)
        
        for i, x in enumerate(walker_1d.walk(pasos_1d)):
            ax.clear()
            walker_1d.draw(ax)
            ax.set_xlabel("Paso")
            ax.set_ylabel("Posición (X)")
            ax.set_title(f"Random Walker 1D - Paso {i + 1} de {pasos_1d}")
            ax.grid(True, alpha=0.3)
            
            chart_placeholder.pyplot(fig)
            time.sleep(velocidad_1d)
        
        st.success(f"¡Simulación completada! Posición final: {walker_1d.x}")

# -----------------------
# PESTAÑA 2D
# -----------------------
with tab2:
    st.header("Random Walker 2D (Coin Flip)")
    st.write("Movimiento en plano 2D según dos lanzamientos de moneda")
    st.write("| Flip 1 | Flip 2 | Resultado |")
    st.write("|--------|--------|-----------|")
    st.write("| Heads | Heads | Arriba |")
    st.write("| Heads | Tails | Derecha |")
    st.write("| Tails | Heads | Izquierda |")
    st.write("| Tails | Tails | Abajo |")
    
    pasos_2d = st.slider("Número de pasos", 10, 500, 100, key="slider_2d")
    velocidad_2d = st.slider("Velocidad (segundos por paso)", 0.01, 0.5, 0.1, key="slider_vel_2d")
    
    start_2d = st.button("Iniciar simulación 2D", key="btn_2d")
    
    if start_2d:
        walker_2d = Walker2D()
        
        fig, ax = plt.subplots(figsize=(8, 8))
        chart_placeholder = st.pyplot(fig)
        
        for i, (x, y) in enumerate(walker_2d.walk(pasos_2d)):
            ax.clear()
            walker_2d.draw(ax)
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_title(f"Random Walker 2D - Paso {i + 1} de {pasos_2d}")
            ax.grid(True, alpha=0.3)
            ax.set_aspect("equal")
            
            chart_placeholder.pyplot(fig)
            time.sleep(velocidad_2d)
        
        st.success(f"¡Simulación completada! Posición final: ({walker_2d.x}, {walker_2d.y})")