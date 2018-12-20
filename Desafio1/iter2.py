from DiccionarioVentas import ventas
def mesesSuperiores(diccionario,numero=45000):
	for mes,valor in diccionario.items():#recorreo los items almacenando los valores en mes y valor
		if valor >=numero:
			print(mes)

mesesSuperiores(ventas,45000)
