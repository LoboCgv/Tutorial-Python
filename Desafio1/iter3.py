import sys
from DiccionarioVentas import ventas#importo diccionario en la libreria

def filtro(diccionario,valor=45000):#funcion recibe un diccionario y un valor para buscar los mayores
#por default uso 45000 según lo solicitado
	res={}#resultado del filtro
	i=0#variable indice de diccionario
	for d in diccionario.values():
		if d>valor:
			res[i]=d#agrego elemento en la posición correspondiente
			i+=1
	return(res)

if(len(sys.argv)==2):
	if(sys.argv[1].isdigit()==True):#aseguro que sea un numero el parametro ingresado
		res=filtro(ventas,float(sys.argv[1]))#llamada a funcion con valor numerico
		print("Resultado filtro")
		print(res)
	else:
		print("Debe ingresar un valor")
else:
	res=filtro(ventas)
	print("Resultado filtro")
	print(res)

