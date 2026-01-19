import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats

st.set_page_config(page_title="Comparación de Dos Grupos", layout="centered")

st.title("📊 Comparación Estadística de Dos Grupos")
st.write(
    "Esta aplicación compara dos grupos considerando diferencias en "
    "tamaño de muestra y varianza, y selecciona automáticamente la prueba estadística adecuada."
)

# -------------------------
# Entrada de datos
# -------------------------
st.header("1️⃣ Ingrese los datos")

grupo_a = st.text_area(
    "Grupo A (valores numéricos separados por coma)",
    "70,72,68,75,71,69,74,73"
)

grupo_b = st.text_area(
    "Grupo B (valores numéricos separados por coma)",
    "65,80,78,60,85,72,90,68,74,77"
)

try:
    A = np.array([float(x) for x in grupo_a.split(",")])
    B = np.array([float(x) for x in grupo_b.split(",")])
except ValueError:
    st.error("⚠️ Asegúrese de ingresar solo números separados por comas.")
    st.stop()

# -------------------------
# Estadística descriptiva
# -------------------------
st.header("2️⃣ Estadística descriptiva")

desc = pd.DataFrame({
    "Grupo": ["A", "B"],
    "Tamaño muestra": [len(A), len(B)],
    "Media": [A.mean(), B.mean()],
    "Desviación estándar": [A.std(ddof=1), B.std(ddof=1)]
})

st.dataframe(desc, use_container_width=True)

# -------------------------
# Prueba de normalidad
# -------------------------
st.header("3️⃣ Prueba de normalidad (Shapiro-Wilk)")

alpha = st.slider("Nivel de significancia (α)", 0.01, 0.10, 0.05)

p_norm_A = stats.shapiro(A).pvalue
p_norm_B = stats.shapiro(B).pvalue

st.write(f"**Grupo A p-valor:** {p_norm_A:.4f}")
st.write(f"**Grupo B p-valor:** {p_norm_B:.4f}")

normal = (p_norm_A > alpha) and (p_norm_B > alpha)

# -------------------------
# Selección de prueba
# -------------------------
st.header("4️⃣ Prueba de hipótesis")

if normal:
    st.subheader("🔹 t de Welch (varianzas y tamaños distintos)")
    stat, p_value = stats.ttest_ind(A, B, equal_var=False)
    test_name = "t de Welch"
else:
    st.subheader("🔹 Mann–Whitney U (no paramétrica)")
    stat, p_value = stats.mannwhitneyu(A, B, alternative="two-sided")
    test_name = "Mann–Whitney U"

st.write(f"**Prueba utilizada:** {test_name}")
st.write(f"**Estadístico:** {stat:.4f}")
st.write(f"**p-valor:** {p_value:.4f}")

# -------------------------
# Interpretación
# -------------------------
st.header("5️⃣ Interpretación")

if p_value < alpha:
    st.success(
        f"📌 Con un nivel de significancia de {alpha}, "
        "existe evidencia estadística para afirmar que los grupos son diferentes."
    )
else:
    st.info(
        f"📌 Con un nivel de significancia de {alpha}, "
        "no existe evidencia suficiente para afirmar que los grupos sean diferentes."
    )

st.markdown(
    """
    **Nota importante:**  
    - Una diferencia estadísticamente significativa no siempre implica relevancia práctica.  
    - La estadística ayuda a tomar decisiones bajo incertidumbre, no a eliminarlas.
    """
)
