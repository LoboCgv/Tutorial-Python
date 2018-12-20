import numpy as np
import pandas as pd

#Carga de archivo csv
archivo='athlete_events.csv'
data=pd.read_csv(archivo)
dataChile=data[data['Team']=='Chile']

#solo los ganadores
ganadores=dataChile[['Name','Year','Medal','Sport']].dropna()
print(ganadores)
masMedallas=ganadores['Year'].value_counts().head(1)
print("año con mas medallas {}".format(masMedallas))

#atletas por año, ya que el team es chile no es necesario hacer comparacion
atletasAnios=dataChile['Year'].value_counts()
print("Competidores por año {}".format(atletasAnios))
maxAtletas=dataChile['Year'].value_counts().head(1)
print("Año con mas participacion{}".format(maxAtletas))
firstMedal=ganadores.sort_values('Year',ascending=True).head(1)
print(firstMedal)
