import streamlit as st
import pandas
import plotly.graph_objects as go
  
st.title("Ejemplo utilización streamlit")
st.markdown("Esto es un poco de markdown")

x = st.slider('x')  # 👈 esto es un widget
st.write(x, 'al cuadrado', x * x)  