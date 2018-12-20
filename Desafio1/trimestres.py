from DiccionarioVentas import ventas
#trimestres

def getValores(diccionario=ventas):
	q1,q2,q3,q4=0,0,0,0#inicializo cada uno de los trimestres
	q1=diccionario.get("Enero")+diccionario.get("Febrero")+diccionario.get("Marzo")#acumulacion de valores| por cada trimestre según corresponde
	q2=diccionario.get("Abril")+diccionario.get("Mayo")+diccionario.get("Junio")
	q3=diccionario.get("Julio")+diccionario.get("Agosto")+diccionario.get("Septiembre")
	q4=diccionario.get("Octubre")+diccionario.get("Noviembre")+diccionario.get("Diciembre")
	valores=[q1,q2,q3,q4]#creacion de lista anidada
	return (valores)
claves=["Q1","Q2","Q3","Q4"]#claves 
quarters=dict(zip(claves,getValores()))#diccionario final
print(quarters)
