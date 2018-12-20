from Diccionario import ventas
import sys

def buscar(diccionario,valor):
	flag=False
	for d in diccionario.values():
		if(d==valor):
			flag=True
	return flag


if(len(sys.argv)>0):
	for i in range(1,len(sys.argv)):
		if buscar(ventas,int(sys.argv[i])):
			print(sys.argv[i])
		else:
			print("No Encontrado")
else:
	print("sin argumentos")
	