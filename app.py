# Importar todas las librearías necesarias
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 
from PIL import Image

image_url = "https://i1.wp.com/entrefronteras.com/wp-content/uploads/2015/06/04.jpg.jpg?resize=600%2C400&ssl=1"
st.image(image_url, caption='Imagen cedidad por https://entrefronteras.com/que-es-la-crisis-de-refugiados/', use_column_width=True)

# Sidebar
# st.image("", caption="Descripción de la imagen")
st.sidebar.header("*Informe sobre personas desplazadas forzosamente a nivel global*")
st.sidebar.markdown(" ")
st.sidebar.markdown("Este informe ha sido realizado por la ONG Data Analysis for Refugees (DAR) con el objetivo de analizar la situación actual de los refugiados a nivel global y predecir los flujos migratorios para años venideors.")
st.sidebar.markdown('Con este informe, se busca generar conciencia sobre la crisis migratoria y promover la colaboración entre gobiernos, organizaciones y ciudadanos para brindar apoyo a los refugiados, así como anticiparse ante futuros desplazamientos y poder erradicar las causas que los provocan y a la vez proveer las condiciones dignas necesarias para las personas desplazadas.')
st.sidebar.markdown('**Fuente de datos:** [UNHCR](https://www.unhcr.org/global-trends-report-2022')
st.sidebar.markdown("**Autores:** Data Analysis for Refugees (DAR)")
st.sidebar.markdown("#Añadir nombres, link a LinkedIn y GitHub")
st.sidebar.markdown("**Version:** 1.0.0")

######################## MAIN  ########################

# Cargar los datos
#url = "URL_DEL_CSV"  # Reemplace con la URL o ruta local de su archivo CSV
#df = pd.read_csv(url)

# Filtrar datos para el año 2022
#df_2022 = df[df['Year'] == 2022]

# Estructura de la aplicación con Streamlit
st.title("*Informe sobre personas desplazadas forzosamente a nivel global*")
st.subheader('Análisis de la serie histórica de los flujos migratorios y situación actual a nivel global y predicciones para los próximos años.')
#st.header("INTRODUCCIÓN")


### ÍNDICE ###
st.markdown("## Aquí irá el índice")


### INTRODUCCIÓN ###
st.markdown("## Introducción")
st.write('Este informe se sumerge en el análisis de las tendencias de series históricas de refugiados y peticiones de asilo, utilizando datos recopilados por ACNUR de gobiernos de todo el mundo. El objetivo es comprender patrones, factores desencadenantes y, fundamentalmente, explorar la posibilidad de prever crisis humanitarias futuras. Al explorar la serie histórica buscamos proporcionar a gobiernos y organizaciones las herramientas necesarias para anticipar y abordar las necesidades básicas de las personas desplazadas, contribuyendo así a construir un futuro más resiliente y compasivo.')


## Primer apartado: Situación general de los refugiados a través de los años
st.header("Evolución del número de personas desplazadas forzosamente a través de los años")
st.write('A continuación, vamos a ver de manera general cómo ha evolucionado el número de personas desplazadas forzosamente a través de los años.')
st.write('Para ello estudiaremos los datos desde el año 1951 hasta el año 2022 e incidiremos en aquellos eventos históricos  que han tenido un mayor impacto en estos datos')

# Ruta del archivo de imagen local
image_path = "graficos/total_refugiados_tiempo.png"
# Mostrar la imagen
st.image(image_path, caption='Evolución del número de refugiados a través de los años', use_column_width=False)

# Ruta del archivo de imagen local
html_path = "graficos/scatter_years.html"
# Mostrar el contenido HTML
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
# Añadir una explicación o caption
explicacion = "Número de desplazados por año y por país de origen"
html_with_caption = f"{html_content}\n\n{explicacion}"

st.components.v1.html(html_content, height=800, width=1000)

# Ruta del archivo de imagen local
image_path3 = "graficos/ARIMA.png"
# Mostrar la imagen
st.image(image_path3, caption='Proyecciones del número de desplazados para los próximos años utilizando el modelo ARIMA', use_column_width=True)

# Ruta del archivo de imagen local
image_path = "graficos/top_10_2022.png"
# Mostrar la imagen
st.image(image_path, caption='Los 10 países con más desplazados forzosos en 2022', use_column_width=False)





st.header("Alguna definiciones de interés")
st.write('**-Refugiados bajo el mandato de ACNUR:** En resumen, un refugiado es una persona que ha cruzado las fronteras internacionales y ha buscado protección en otro país porque enfrenta amenazas graves en su país de origen.')
st.write('**-Solicitantes de asilo:** individuos que han buscado protección internacional y cuyas solicitudes de estatus de refugiado aún no han sido determinadas.')
st.write('**-Personas desplazadas internas:** son personas o grupos de personas que han sido obligadas u obligadas a huir o abandonar sus hogares, debido a conflictos armados, situaciones de violencia generalizada, violaciones de los derechos humanos o desastres naturales, y que no han cruzado una frontera estatal reconocida internacionalmente.')
st.write('**-Otras personas que necesitan protección internacional:** han sido desplazadas forzosamente a través de fronteras internacionales, que no han sido informadas bajo otras categorías (solicitantes de asilo, refugiados, personas en situaciones similares a las de los refugiados) pero que probablemente necesitan protección internacional.')
st.write('**-Otras personas de interés para ACNUR:** no necesariamente encajan directamente en ninguno de estos grupos anteriores, pero a quienes el ACNUR ha extendido sus servicios de protección y/o asistencia, basándose en motivos humanitarios.')



## Subtítulo 1
st.header("El Estado Actual de los Refugiados Globales")
st.write("En el año 2022, el mundo enfrenta una crisis migratoria con un total de 110 millones de refugiados. Este informe detalla la situación actual, destacando los países de origen y los principales destinos.")


## Subtítulo 2
st.header("Países de Origen Predominantes")

st.subheader("1. Afganistán")
st.write("A pesar de los esfuerzos internacionales, Afganistán continúa siendo uno de los principales países de origen de refugiados, con un flujo constante debido a conflictos y desplazamientos.")

st.subheader("2. Venezuela")
st.write("La situación política y económica en Venezuela ha llevado a un significativo éxodo de personas, contribuyendo sustancialmente al número global de refugiados.")

st.subheader("3. Siria")
st.write("Los conflictos en Siria persisten, haciendo que la población busque refugio en otras naciones en busca de seguridad y estabilidad.")

st.subheader("4. Ucrania")
st.write("A pesar de los acontecimientos en años anteriores, Ucrania sigue siendo un punto de origen para aquellos que buscan seguridad en medio de tensiones políticas y sociales.")



## Subtítulo 3
st.header("Principales Destinos de Refugiados")

st.subheader("1. Reino Unido (UK)")
st.write("Como uno de los destinos principales, el Reino Unido experimenta un flujo constante de refugiados que buscan nuevas oportunidades y seguridad.")

st.subheader("2. Estados Unidos (USA)")
st.write("La búsqueda del 'sueño americano' sigue atrayendo a personas de diversas partes del mundo, contribuyendo a la cifra global de refugiados.")

st.subheader("3. Rusia")
st.write("Aunque históricamente ha sido un país de origen, Rusia también se destaca como receptor de refugiados, desempeñando un papel crucial en la dinámica migratoria global.")

## Subtítulo 4
st.header("Proyecciones para el Año 2023")
st.write("Con base en modelos de machine learning y análisis de tendencias, se proyecta que la cifra de refugiados podría experimentar cambios significativos en 2023. Este informe ofrece una visión anticipada de las posibles alteraciones en los flujos migratorios y destinos emergentes.")





# Peticiones de asilo
st.header("Peticiones de asilo")
# Explorar datos sobre peticiones de asilo a lo largo del tiempo.
# Identificar patrones regionales y cambios significativos.
# Analizar factores que podrían haber influido en las peticiones de asilo.
# Peticiones totales
# Distribución por sexo/género
# Distribución de 2-3 paises de origen y 2-3 de destino para ver cómo se aprueban/rechazan peticiones


# Situación actual de los refugiados
st.header("Situación actual de los refugiados")
# Describir la situación actual de los movimientos de refugiados en 2023.
# Destacar cifras clave y regiones más afectadas.
# .
# Datos de refugiados en el último año
# Mapas para ver de dónde son y a dónde van


## Predicciones
st.header("Qué esperamos para los próximos años")
st.write("En base a modelos de machine learning y análisis de tendencias, se proyecta que la cifra de refugiados podría experimentar cambios significativos en 2023. Este informe ofrece una visión anticipada de las posibles alteraciones en los flujos migratorios y destinos emergentes.")

