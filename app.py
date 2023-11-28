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
# Información del autor
autor_nombre_ioa = "Ioana Cretu"
autor_correo_ioa = "ioana.cretu22@gmail.com"
autor_github_ioa = "https://github.com/IoanaCretuAndrei"
autor_linkedin_ioa = "https://www.linkedin.com/in/ioana-cretu-cyta/"

# Información del autor
autor_nombre_ign = 'Ignacio Lázaro'
autor_correo_ign = "ignaciolazaro80@gmail.com"
autor_github_ign = "https://github.com/ignalazaro"
autor_linkedin_ign = "https://www.linkedin.com/in/ignaciolázaro/"

# Mostrar en la barra lateral



st.sidebar.header("*Informe sobre personas desplazadas forzosamente a nivel global*")
st.sidebar.markdown(" ")
st.sidebar.markdown("Este informe ha sido realizado por la ONG Data Analysis for Refugees (DAR) con el objetivo de analizar la situación actual de los refugiados a nivel global y predecir los flujos migratorios para años venideors.")
st.sidebar.markdown('Con este informe, se busca generar conciencia sobre la crisis migratoria y promover la colaboración entre gobiernos, organizaciones y ciudadanos para brindar apoyo a los refugiados, así como anticiparse ante futuros desplazamientos y poder erradicar las causas que los provocan y a la vez proveer las condiciones dignas necesarias para las personas desplazadas.')
st.sidebar.markdown('**Fuente de datos:** [UNHCR](https://www.unhcr.org/global-trends-report-2022')
st.sidebar.markdown("**Autores:** Data Analysis for Refugees (DAR)")
st.sidebar.write(f"**Autor/a:** {autor_nombre_ioa}")
st.sidebar.write(f"**Correo:** {autor_correo_ioa}")
st.sidebar.write(f"**GitHub:** [{autor_github_ioa}]({autor_github_ioa})")
st.sidebar.write(f"**LinkedIn:** [{autor_linkedin_ioa}]({autor_linkedin_ioa})")
st.sidebar.write(f"**Autor/a:** {autor_nombre_ign}")
st.sidebar.write(f"**Correo:** {autor_correo_ign}")
st.sidebar.write(f"**GitHub:** [{autor_github_ign}]({autor_github_ign})")
st.sidebar.write(f"**LinkedIn:** [{autor_linkedin_ign}]({autor_linkedin_ign})")
st.sidebar.markdown("**Version:** 1.0.0")



######################## MAIN  ########################


# Estructura de la aplicación con Streamlit
st.title("*Informe sobre personas desplazadas forzosamente a nivel global*")
st.subheader('Análisis de la serie histórica de los flujos migratorios y situación actual a nivel global y predicciones para los próximos años.')


### INTRODUCCIÓN ###
st.markdown("## Introducción")
st.write('Este informe se sumerge en el análisis de las tendencias de series históricas de refugiados y peticiones de asilo, utilizando datos recopilados por ACNUR de gobiernos de todo el mundo. El objetivo es comprender patrones, factores desencadenantes y, fundamentalmente, explorar la posibilidad de prever crisis humanitarias futuras. Al explorar la serie histórica buscamos proporcionar a gobiernos y organizaciones las herramientas necesarias para anticipar y abordar las necesidades básicas de las personas desplazadas, contribuyendo así a construir un futuro más resiliente y compasivo.')


## Primer apartado: Situación general de los refugiados a través de los años

st.header("Evolución del número de personas desplazadas forzosamente a través de los años")
st.subheader('¿Qué entendemos por desplazamiento forzoso?')
st.write('La ACNUR hace una clasificación de las personas forzadas a desplazarse, agrupándolas en diferentes categorías: ')
st.write('**-Refugiados bajo el mandato de ACNUR:**  un refugiado es una persona que ha cruzado las fronteras internacionales y ha buscado protección en otro país porque enfrenta amenazas graves en su país de origen.')
st.write('**-Solicitantes de asilo:** individuos que han buscado protección internacional y cuyas solicitudes de estatus de refugiado aún no han sido determinadas.')
st.write('**-Personas desplazadas internas:** son personas o grupos de personas que han sido obligadas u obligadas a huir o abandonar sus hogares, debido a conflictos armados, situaciones de violencia generalizada, violaciones de los derechos humanos o desastres naturales, y que no han cruzado una frontera estatal reconocida internacionalmente.')
st.write('**-Otras personas que necesitan protección internacional:** han sido desplazadas forzosamente a través de fronteras internacionales, que no han sido informadas bajo otras categorías (solicitantes de asilo, refugiados, personas en situaciones similares a las de los refugiados) pero que probablemente necesitan protección internacional.')
st.write('**-Otras personas de interés para ACNUR:** no necesariamente encajan directamente en ninguno de estos grupos anteriores, pero a quienes el ACNUR ha extendido sus servicios de protección y/o asistencia, basándose en motivos humanitarios.')
st.write('Para este estudio se ha calculado como Total de desplazamientos forzados’ la suma de estas 5 categorías.')
st.subheader('Evolución del número de personas desplazadas forzosamente a través de los años')
st.write('A continuación, vamos a ver de manera general cómo ha evolucionado el número de personas desplazadas forzosamente a través de los años.')
st.write('Para ello estudiaremos los datos desde el año 1951 hasta el año 2022 e incidiremos en aquellos eventos históricos  que han tenido un mayor impacto en estos datos')
st.write('En este primer gráfico podemos ver una representación del total de desplazamientos forzados desde el año 1951 hasta la actualidad.')

# Ruta del archivo de imagen local
image_path = "graficos/total_refugiados_tiempo.png"
# Mostrar la imagen
st.image(image_path, caption='Evolución del número de refugiados a través de los años', use_column_width=True)

st.subheader('Desplazamientos forzosos por continente y año')
st.write('En este gráfico interactivo, podemos la evolución de los desplazamientos forzados por países y año. Los tamaños de los circulos son proporcionales al número de desplazamientos forzados procedentes de cada país.')
st.write('Estos datos pueden relacionarse con algunos hechos históricos que han tenido un gran impacto en el número de desplazamientos forzados, como por ejemplo: ')

# Ruta del archivo de imagen local
html_path = "graficos/scatter_years.html"
# Mostrar el contenido HTML
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
# Añadir una explicación o caption
explicacion = "Número de desplazados por año y por país de origen"
html_with_caption = f"{html_content}\n\n{explicacion}"
st.components.v1.html(html_content, height=500, width=850)


events = ['-1974-1991: La guerra civil Etíope',
        '-1994: El genocidio de Ruanda',
        '-2003-2011: La guerra de Irak',
        '-2011: La guerra de Siria',
        '-2022: La guerra de Ucrania',
        '-1979-1989: La invasión soviética de Afganistán',
        '-1989-1992: La guerra de Afgana',
        '-2001-2021: La guerra de Afganistán'
]
for event in events:
    st.write(event)
    




st.subheader('Desplazamientos forzosos por continente y año')
st.write('En este gráfico podemos ver como han ido aumentando los números totales de personas forzadas a desplazarse, por continente')
st.write('A continuación, podemos ver los principales continentes de asilo de estos desplazamientos forzados.')

# Ruta del archivo de imagen local
html_path = "graficos/bar_continent_origin.html"
# Mostrar el contenido HTML
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
# Añadir una explicación o caption
explicacion = "Número de desplazados por año y por país de origen"
html_with_caption = f"{html_content}\n\n{explicacion}"
st.components.v1.html(html_content, height=450, width=850)


html_path = "graficos/bar_continent_asylum.html"
# Mostrar el contenido HTML
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
# Añadir una explicación o caption
explicacion = "Número de desplazados por año y por país de origen"
html_with_caption = f"{html_content}\n\n{explicacion}"
st.components.v1.html(html_content, height=450, width=850)

###### Peticiones de asilo ######

st.header("Peticiones de asilo")
st.write("En este apartado vamos a analizar las peticiones de asilo a lo largo de los años, la demografía de los solicitantes y cómo se han resuelto estas de forma variable.")
st.write('En primer lugar vamos a analizar, para tener una mejor visión general, tanto los países que más peticiones de asilo han recibido cómo los páises de origen de estas')

# Ruta del archivo de imagen local
image_path = "graficos/top_asilo_destino.png"
# Mostrar la imagen
st.image(image_path, caption='Porcentajes de peticiones recibidas totales por los 15 países con más peticiones recibidas', use_column_width=False)

# Ruta del archivo de imagen local
image_path = "graficos/top_asilo_origen.png"
# Mostrar la imagen
st.image(image_path, caption='Porcentajes de por país de origen del total de peticiones solicitadas', use_column_width=False)

st.write('Seguidamente, veamos cómo es demográficamente la población que solicita asilo')
st.write('Contrariamente a lo que se podría pensar, no hay una gran diferencia entre el número de hombres y mujeres que solicitan asilo')
# Ruta del archivo de imagen local
image_path = "graficos/Sexos_refugees.png"
# Mostrar la imagen
st.image(image_path, caption='Distribución por sexos de personas solicitantes de asilo', use_column_width=True)
# Ruta del archivo de imagen local
image_path = "graficos/edad_hombres.png"
# Mostrar la imagen
st.image(image_path, caption='Distribución per edad de los hombres solicitantes de asilo', use_column_width=True)
st.write('En cuanto a la edad, hay que enfatizar que la mayoría de las personas que solicitan asilo son jóvenes menores de 17 años, representando casi la mitad de las solicitudes')
st.write('Estos datos nos preocupan especialmente, ya que los menores de edad especialmente vulnerables y que requieren de una atención especial')
# Ruta del archivo de imagen local
image_path = "graficos/edad.png"
# Mostrar la imagen
st.image(image_path, caption='Distribución per edad de las mujeres solicitantes de asilo', use_column_width=True)

st.write('Una vez ya tenemos una visión más general y sabemos cuáles son los países que más peticiones de asilo reciben y de dónde provienen, vamos a analizar cómo se han resuelto estas peticiones a lo largo de los años')
st.write('En primera instancia, vamos a ver cómo se han resuelto las peticiones de asilo de los 4 países de origen con más solicitudes en sus principales destinos')
# Ruta del archivo de imagen local
image_path = 'graficos/asilo_origen.png'
# Mostrar la imagen
st.image(image_path, caption='Solicitudes de asilo por país de origen enen sus top destinos', use_column_width=True)

st.write('A continuación, vamos a ver cómo los 4 países con más peticiones de asilo recibidas han resuelto estas según de dónde provenían.')
# Ruta del archivo de imagen local
image_path = 'graficos/asilo_destino.png'
# Mostrar la imagen
st.image(image_path, caption='Solicitudes de asilo recibidas por país de origen', use_column_width=True)

html_path = "graficos/dualmap.html"
# Mostrar el contenido HTML
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
st.components.v1.html(html_content, height=600, width=800)


############ SITUACION 2022 #################

st.header("Situación de los desplazamientos forzados en 2022")

st.write("En este apartado vamos a analizar la situación actual de los refugiados en 2022, destacando los países de origen y los principales destinos.")
st.write('Esta gráfica representa los 10 países de origen con mayores índices de desplazamientos forzados en el año 2022')

# Ruta del archivo de imagen local
image_path = "graficos/top_10_2022.png"
# Mostrar la imagen
st.image(image_path, caption='Los 10 países con más desplazados forzosos en 2022', use_column_width=False)

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

st.write('Por último, se han representado los cuatro países con mas desplazados forzosos en un mapa interactivo, donde podemos ver también los 10 principales países de asilo para cada uno de estos países.')


# Ruta del archivo de imagen local
html_path = "graficos/mapa_asylum_2022.html"
# Mostrar el contenido HTML
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
# Añadir una explicación o caption
explicacion = "Número de desplazados por año y por país de origen"
html_with_caption = f"{html_content}\n\n{explicacion}"
st.components.v1.html(html_content, height=600, width=800)

# Describir la situación actual de los movimientos de refugiados en 2023.
# Destacar cifras clave y regiones más afectadas.
# .
# Datos de refugiados en el último año
# Mapas para ver de dónde son y a dónde van


####### PREDICCIONES#########
st.header("Qué esperamos para los próximos años")
st.write("En base a modelos de machine learning y análisis de tendencias, se proyecta que la cifra de refugiados podría experimentar cambios significativos en 2023. Este informe ofrece una visión anticipada de las posibles alteraciones en los flujos migratorios y destinos emergentes.")

# Ruta del archivo de imagen local
image_path3 = "graficos/ARIMA.png"
# Mostrar la imagen
st.image(image_path3, caption='Proyecciones del número de desplazados para los próximos años utilizando el modelo ARIMA', use_column_width=True)