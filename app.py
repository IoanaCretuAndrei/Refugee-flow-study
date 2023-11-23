import streamlit as st

import pandas as pd

# Sidebar
# st.image("", caption="Descripción de la imagen")
st.sidebar.header("Bienvenidos!")
st.sidebar.markdown(" ")
st.sidebar.markdown("*Informe de Flujos Migratorios 2022 y Predicciones para 2023.*")

st.sidebar.markdown("**Version:** 1.0.0")




# Cargar los datos
#url = "URL_DEL_CSV"  # Reemplace con la URL o ruta local de su archivo CSV
#df = pd.read_csv(url)

# Filtrar datos para el año 2022
#df_2022 = df[df['Year'] == 2022]

# Estructura de la aplicación con Streamlit
st.title("Informe de Flujos Migratorios 2022 y Predicciones para 2023")

## Subtítulo 1
st.header("El Estado Actual de los Refugiados Globales")
st.write("En el año 2022, el mundo enfrenta una crisis migratoria con un total de 110 millones de refugiados. Este informe detalla la situación actual, destacando los países de origen y los principales destinos.")

## Subtítulo 2
st.header("Países de Origen Predominantes")

### Afganistán
st.subheader("1. Afganistán")
st.write("A pesar de los esfuerzos internacionales, Afganistán continúa siendo uno de los principales países de origen de refugiados, con un flujo constante debido a conflictos y desplazamientos.")

### Venezuela
st.subheader("2. Venezuela")
st.write("La situación política y económica en Venezuela ha llevado a un significativo éxodo de personas, contribuyendo sustancialmente al número global de refugiados.")

### Siria
st.subheader("3. Siria")
st.write("Los conflictos en Siria persisten, haciendo que la población busque refugio en otras naciones en busca de seguridad y estabilidad.")

### Ucrania
st.subheader("4. Ucrania")
st.write("A pesar de los acontecimientos en años anteriores, Ucrania sigue siendo un punto de origen para aquellos que buscan seguridad en medio de tensiones políticas y sociales.")

## Subtítulo 3
st.header("Principales Destinos de Refugiados")

### Reino Unido
st.subheader("1. Reino Unido (UK)")
st.write("Como uno de los destinos principales, el Reino Unido experimenta un flujo constante de refugiados que buscan nuevas oportunidades y seguridad.")

### Estados Unidos
st.subheader("2. Estados Unidos (USA)")
st.write("La búsqueda del 'sueño americano' sigue atrayendo a personas de diversas partes del mundo, contribuyendo a la cifra global de refugiados.")

### Rusia
st.subheader("3. Rusia")
st.write("Aunque históricamente ha sido un país de origen, Rusia también se destaca como receptor de refugiados, desempeñando un papel crucial en la dinámica migratoria global.")

## Subtítulo 4
st.header("Proyecciones para el Año 2023")
st.write("Con base en modelos de machine learning y análisis de tendencias, se proyecta que la cifra de refugiados podría experimentar cambios significativos en 2023. Este informe ofrece una visión anticipada de las posibles alteraciones en los flujos migratorios y destinos emergentes.")

# Visualización de datos
st.subheader("Datos para el año 2022")
#st.dataframe(df_2022)

# Puede agregar más visualizaciones y secciones según sea necesario.

# Finalmente, ejecutar la aplicación con el siguiente comando en la terminal
# streamlit run app.py
