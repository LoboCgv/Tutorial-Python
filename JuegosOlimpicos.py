import numpy as np
import pandas as pd

def report(df,var,gender='Female'):
	for i in df[gender].unique():
		print(df[var].mean())

#Carga de archivo csv
archivo='athlete_events.csv'
data=pd.read_csv(archivo)

#se obtiene tupla con el tamaño de filas y columnas
registros,campos=data.shape[0],data.shape[1]
print("registros {} campos {}".format(registros,campos))
#Calcula cantidad de competencias realizadas. se obtiene una tupla
competencias=data['Year'].unique().shape[0]
print("competencias realizadas {}".format(competencias))
#distribución de competencias verano o invierno
print(data['Season'].value_counts('%')*100)
#año y lugar competencias verano
competenciasOrden=data.sort_values('Year',ascending=True).where(data['Season']=='Summer')
print("Verano año: {} lugar:{}".format(competenciasOrden['Year'].head(1),competenciasOrden['City'].head(1)) )
#año y lugar competencias invierno... dropna no considera NaN
competenciasOrden=data.sort_values('Year',ascending=True).where(data['Season']=='Winter').dropna()
print("Verano año: {} lugar:{}".format(competenciasOrden['Year'].head(1),competenciasOrden['City'].head(1)) )
#competidores por pais
competidoresPais=data['Team'].value_counts()[:10]
print(competidoresPais)
#medallas por pais
medallas=data['Medal'].value_counts('%')
print(medallas)
#paises participantes primera olimpiada de verano
paisesVerano1=data.sort_values('Year',ascending=True).where(data['Season']=='Summer')['Team'].unique()
print(paisesVerano1)

#nuevas tablas para distribuciones
oroData=data[data['Medal']=='Gold']
print(oroData)
oroBronce=data[data['Medal']=='Bronze']
print(oroBronce)
silverData=data[data['Medal']=='Silver']
print(silverData)
naNData=data[data['Medal']!='NaN']
print(naNData)
#agregar columna con asignacion de 1 cuando esmujer y 0 para hombre
oroData['Female']= np.where(oroData['Sex']=='F', 1, 0)
oroBronce['Female']= np.where(oroBronce['Sex']=='F', 1, 0)
silverData['Female']= np.where(silverData['Sex']=='F', 1, 0)
naNData['Female']= np.where(naNData['Sex']=='F', 1, 0)
data['Female']= np.where(data['Sex']=='F', 1, 0)
#los paises con más medallas por cada categoria 10 primeros
print(oroData['Team'].value_counts().head(10))
print(oroBronce['Team'].value_counts().head(10))
print(silverData['Team'].value_counts().head(10))
print(naNData['Team'].value_counts().head(10))

print("##########################")
#distribucion entre hombres y mujeres
print(oroData['Sex'].value_counts())
print(oroBronce['Sex'].value_counts())
print(silverData['Sex'].value_counts())
print(naNData['Sex'].value_counts())

print("##########################")
report(data,'Height')