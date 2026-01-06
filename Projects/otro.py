import streamlit as st
import numpy as np
import plotly.express as px

st.title("Proceso Markoviano: Caminata Aleatoria")

n = st.slider("Número de pasos", 10, 500, 100)

steps = np.random.choice([-1, 1], size=n)
path = np.cumsum(steps)

fig = px.line(path, labels={"value": "Estado", "index": "Tiempo"})
st.plotly_chart(fig)
