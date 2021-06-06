import streamlit as st
import pandas
import plotly.graph_objects as go
  
st.title("Ejemplo utilización streamlit")
st.markdown("Este ejemplo muestra cómo utilizar streamlit para mostrar datos de DataFrames Pandas en una aplicación web")
st.sidebar.title("Seleccionar gráficas")
st.sidebar.markdown("Selecciona el tipo de gráfica que quieras mostrar:")
  
df = pandas.read_csv("https://raw.githubusercontent.com/kirenz/datasets/master/gapminder.csv")
  
chart_visual = st.sidebar.selectbox('Seleccionar gráfica', 
                                    ('Line Chart', 'Bar Chart', 'Pie Chart'))
#marcadores = st.sidebar.checkbox("Mostrar marcadores", True)

fig = go.Figure()
#if marcadores:
#        smarcadores = "lines+markers"
#else:
#        smarcadores = "lines"

st.line_chart(df)

if chart_visual == 'Line Chart':
        df2 = df[df["country"] == 'Spain']
        fig.add_trace(go.Scatter(x = df2["year"], y = df2["pop"],
                                 mode = "lines"))

#        fig.add_trace(go.Scatter(x = df2["year"], y = df2["pop"],
#                                 mode = smarcadores))

        fig.update_layout(title='Evolución Población España',
                   xaxis_title='Año',
                   yaxis_title='Población (millones)')
        st.plotly_chart(fig, use_container_width=True)


if chart_visual == 'Bar Chart':
        df2 = df[df["year"] == 2007]
        fig.add_trace(go.Bar(x = df2.iloc[0:10].country, y = df2.iloc[0:10].lifeExp))
        fig.update_layout(title='Expectativa de vida en años')
        st.plotly_chart(fig, use_container_width=True)

if chart_visual == 'Pie Chart':
        df2 = df[df["year"] == 2007].groupby("continent").sum()
        fig.add_trace(go.Pie(labels=df2["pop"].keys(), values=df2["pop"]))
        fig.update_layout(title='Porcentajes de población por continente')
        st.plotly_chart(fig, use_container_width=True)

