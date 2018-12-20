from Diccionario import ventas
for v in ventas.values():
	if(v>=45000):
		print(v)
#meses donde las ventas son mayores a 45000
for mes,valor in ventas.items():
	if valor >=45000:
		print(mes)
		
#mayores que
valor=int(input("valor filtro"))
def filtro(diccionario,valor):
	for d in diccionario.values():
		if d>valor:
			print (d)

filtro(ventas,valor)