import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Proyecto Sprint 7 - Análisis Exploratorio de Datos (EDA) de Vehículos en EE.UU.
st.header("Análisis Exploratorio de Datos de Vehículos en EE.UU.")

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# crear una casilla de verificación de histograma
build_histogram = st.checkbox('Construir un histograma')
# crear una casilla de verificación de dispersión
build_scatter = st.checkbox('Construir un diagrama de dispersión')

# Crear un botón en la aplicación Streamlit
show_diagram_button = st.button('Construir diagrama selecionado')

# Lógica a ejecutar cuando se hace clic en el botón
if show_diagram_button:
    if build_histogram:  # si la casilla de verificación histograma está seleccionada
        # Escribir un mensaje en la aplicación
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

        # Crear un histograma utilizando plotly.graph_objects
        # Se crea una figura vacía y luego se añade un rastro de histograma
        fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

        # Agregamos un título al gráfico
        fig.update_layout(title_text='Distribución del Odómetro')

        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
        # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, use_container_width=True)

    elif build_scatter:  # si la casilla de verificación dispersión está seleccionada
        # Escribir un mensaje en la aplicación
        st.write(
            'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

        # Crear un diagrama de dispersión utilizando plotly.graph_objects
        fig = go.Figure(data=go.Scatter(
            x=car_data['odometer'],
            y=car_data['price'],
            mode='markers'  # Modo de marcador para puntos individuales
        ))

        # Agregamos un título al gráfico y etiquetas a los ejes
        fig.update_layout(
            title_text='Diagrama de Dispersión del Precio vs Año',
            xaxis_title='Año',
            yaxis_title='Precio'
        )

        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
        st.plotly_chart(fig, use_container_width=True)

    elif not build_histogram and not build_scatter:
        st.write('Por favor, seleccione al menos un tipo de diagrama para construir.')

    elif build_histogram and build_scatter:
        st.write('Por favor, seleccione solo un tipo de diagrama a la vez.')
