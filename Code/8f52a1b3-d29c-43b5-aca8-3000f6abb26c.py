

#INTRODUCCION

# En este proyecto estaremos realizando la continuidad del analisis que se está llevando a cabo en la Ciudad de Chicago, para averiguar mediante el análisis con python, cuáles son los efectos que tiene el clima  en los viajes  durante los días 15 y 16 de Noviembre en diversas compañías, destinos y horas en las que se inició el viaje.
# De igual forma se estarán realizando tablas comparativas, filtrados, revisión de datos y análisis estadístico para sacar la mayor cantidad de información que nos sea útil para responder ciertas custiones de nuestro interés.


#Analisis exploratorio en Python

# Importación de librerías

# En esta parte del proyecto vamos a continuar analizando los datos de las tareas anteriores, en esta parte se van a incluir dos datasets, los cuales nos van a proveer la información relacionada a las compañias de taxis y a los viajes.
# En este proyecto estudiaremos el comportamiento de cada uno de los datos de las compañias para dar más información acerca de los viajes, la duración, así como las características que afectan la duración de cada uno de ellos.

import pandas as pd  #Primero hay que importar todas las librerías que nos son útiles para el analisis.
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime as dt
from scipy import stats as st


df_company=pd.read_csv('C:/Users/carlo/OneDrive/Documentos/Project- Trips Data/Datasets/moved_project_sql_result_01.csv') #Se importa el datset relacionado a las compañias
df_trip=pd.read_csv('C:/Users/carlo/OneDrive/Documentos/Project- Trips Data/Datasets/moved_project_sql_result_04.csv') #Se importa el dataset relacionado a las características de los viajes
df_duration=pd.read_csv('C:/Users/carlo/OneDrive/Documentos/Project- Trips Data/Datasets/moved_project_sql_result_07.csv')# Se importa el dataset relacionado a la duración de los viajes


# ##  Análisis y Filtrado de Datos
# En esta sección nos vamos a encargar de revisar, analizar y corregir los dataframes creados para asegurarnos que la información a usar y a seleccionar sea la correcta.
# Análisis de Dataframe de compañias

df_company.info() #Revisar el primer Df para verificar que los datos estén correctos, que no existan valores ausentes o duplicados y que los datos estén con las caracteristicas que uno busca
df_company.head() #Revisar los encabezados
df_company.describe() #Infromación estadística de las compañias
df_company.duplicated().sum() # Corroborar que no tengan duplicados

# Análisis de Dataframe de viajes

df_trip.info()#Revisar el  Df para verificar que los datos estén correctos, que no existan valores ausentes o duplicados y que los datos estén con las caracteristicas que uno busca
df_trip.duplicated().sum()# Revisar que no tengamos que no tengamos duplicados
df_trip.describe() #Obetener información estadística del dataframe de los viajes


# ### Análisis de Dataframe de Duración

df_duration.info() #Revisar el primer Df para verificar que los datos estén correctos, que no existan valores ausentes o duplicados y que los datos estén con las caracteristicas que uno busca
df_duration.duplicated().sum() #En este dataframe si encontramos duplicados
df_duration.describe() #Obtención de información estadística de la duración de los viajes

df_duration.drop_duplicates(inplace=True) #Eliminar los duplicados


# Una vez que ya tenemos los datos justo como los necesitamos para realizar el análisis, podemos comentar que no encontramos datos faltantes, sólo duplicados que ya fueron eliminados, no se encontró tampoco que los encabezados de las columnas estuviesen mal o que tuvieran espacios innecesarios.
# Por otro lados los dataframes hacen referencia al nombre por compañia, así como la totalidad de los viajes hechos por cada una de ellas, el promedio de cada uno de ellos y también nos muestra la hora, la fecha y las condiciones de los viajes.


#Creación de Tablas comparativas

# En esta sección estaremos creando un conjunto de tablas que nos muestren evidencia del comportamiento de los viajes terminados hacia los destinos al igual nos dará la información de cuales son las 10 compañias que más viajes realizan.


df_company_popular=df_company.head(10) #Quise crear otro dataframe para las 10 primeras compañías con más cantidad de viajes
df_company_popular #Mostrar la tabla 


#Tabla de las compañias más populares 

df_company_popular.plot(kind='barh',x='company_name',xlabel='Companies',ylabel='Amount of trips',title='Most popular companies')

# En este gráfico podemos observar las 10 compañias con más cantidad de viajes de manera descendente, de manera que Flash cab es la compañia de taxis que más viajes tiene sobre las otras, con más de 18000 viajes, siendo la lider de toda la tabla, destacando de que se tiene una dominancia muy sobresaliente sobre las demás.




# Tabla de los destinos más populares

df_trip_popular=df_trip.head(10) #Filtrar los 10 destinos más populares para analizar el gráfico.
df_trip_popular #Mostrar la tabla a trabajar

df_trip_popular.plot(kind='barh',x='dropoff_location_name',xlabel='Locations',ylabel='Average Trips',title='Most Popular Locations')

# Como podemos ver en el gráfico de arriba, los barrios que son usados como destinos finales por los usuarios están concentrados en 10 destinos populares, siendo el "Loop" el destino más popular sobre todos los demás, estando 'River North" y "Streeterville como el tecero.
# Esto nos sirve para obtener una información más completa acerca de los barrios de Chicago y de sus compañias, los cual nos brinda un servicio más completo, ya que esta información nos permite asignar más recursos de taxis o unidades a destinos más concurridos, asi como analizar que características tienen las compañias que mayor numero de viajes tienen sobre las que no tienen tantas.



#Análisis estadístico


# En esta parte estaremos analizando los datos sobre los viajes realizados desde Loop hasta el aeropuerto O'Hare.

#Filtrado de las muestras

df_duration.head() #Mostrar las primeras columnas del dataframe con el que trabajaremos

df_duration['start_ts']=pd.to_datetime(df_duration['start_ts']) #Convertimos a formato date para poder manipular los datos
df_lluvioso=df_duration[(df_duration['start_ts'].dt.dayofweek==5)&(df_duration['weather_conditions']=='Bad')] #Filtramos por sábado y por condiciones de día lluvioso
media_lluvioso=df_lluvioso['duration_seconds'] #Filtrar muestras
df_lluvioso.head() #Muestras para los días lluviosos

df_no_lluvioso=df_duration[(df_duration['start_ts'].dt.dayofweek==5)&(df_duration['weather_conditions']=='Good')] #Filtramos por sábado y por un día bueno
media_no_lluvioso=df_no_lluvioso['duration_seconds']
df_no_lluvioso.head() #Muestras para los días buenos


# En esta parte dejamos los dataframes listos de manera que podamos utilizarlos para analizar su comportamiento del destino del Loop hasta el aeropuerto O´Hare con un día lluvioso un sábado.
# En este caso filtre para crear un dataframe con la información de que sea sábado y que la condición del clima sea lluviosa, corroboré que las fechas estuviesen bien y chequé el calendario.
# De igual forma cree el dataframe contrario de que fuese también sábado pero que no fuese lluvioso.


#Prueba de levene
 
# En esta sección analizaremos las varianzas de las muestras para verificar sin son iguales o son distintas entre ellas para después pasar al analisis esatdístico mediante la prueba de hipótesis
# Realizaremos una prueba de levene para las varianzas de los grupos de los días lluviosos contra los días que no llueven, generando las hipotesis de la siguiente manera:


# Hipótesis Nula (H0):La varianza de ambos grupos es igual.
# Hipótesis Alternativa (H1): La varianza de al menos uno de los grupos es diferente

variance_test= st.levene(media_lluvioso,media_no_lluvioso)
variance_test.statistic

alpha=0.05 #Nivel de significancia 

if variance_test.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print('No podemos rechazar la hipotesis nula')


# Conclusión prueba de levene
 
# Al no poder rechazarla hipotesis nula no hay suficiente evidencia para afirmar que las varianzas de ambos grupos son diferentes.



#Prueba de Hipótesis

# En este caso una vez que tenemos las medias listas y filtradas por el sábado lluvioso contra el sábado que no lleuve, pasaré a realizar el análisis estadístico por lo que pasaré a plantear las hipotésis de la siguiente manera:
 
# Hipótesis Nula (H0): No hay diferencia significativa en la duración promedio de los viajes el día sábado  entre días lluviosos y no lluviosos.
# Hipótesis Alternativa (H1): Hay una diferencia significativa en la duración promedio de los viajes  el día entre días lluviosos y no lluviosos.


alpha=0.05 #Nivel de significancia

results=st.ttest_ind(media_lluvioso,media_no_lluvioso,equal_var=True)

print('valor p:',results.pvalue)

if results.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print('No podemos rechazar la hipotesis nula')

#Conclusón de Prueba de Hipótesis
 
# Con esto podemos concluir que al rechazar la hipotesis nula hay una diferencia significativa en la duración promedio en los viajes que son realizado los sábados cuando llueve, por lo que podemos decir que la lluvia realmente afecta la duración de un viaje los sábados.
# 

# ## Conclusión

# Con este proyecto podemos observar que compañias de taxis son las que más viajes tienen, por lo que esa información de negocio puede ser utilizada para invertir en más unidades que estén relacioandas con los destinos más frecuentados, así como considerar que los días lluviosos hacen que el servicio tarde más, por lo que esa información viene bien a una compañia para tener un plan para días como ese y tener considerado que acciones tomar para eventos en tales condiciones.
# De igual forma las información nos da para realizarns el cuestionamiento de que las compañías que tienen pocos viajes pero que a la mejor sus viajes no varían en gran consideraación en tiempo, podrían pensar en revisar que condiciones del servicio podrían mejorar o añadir para atraer más clientes y mejorar sus ingresos conforme el paso del tiempo.

