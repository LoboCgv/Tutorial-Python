from DiccionarioVentas import ventas
def valoresSuperiores(diccionario,valor=45000):#por defecto se trabaja con lo solicitado
	for v in diccionario.values():#sólo se recorren los valores
		if(v>=valor):#al cumplir condicion se escribe por pantalla
			print(v)

valoresSuperiores(ventas,45000)
