from DiccionarioVentas import ventas
import sys

if(len(sys.argv)>1):#se debe contar con al menops un argumento
	for i in range(1,len(sys.argv)):#recorro los argumentos 
		if(sys.argv[i].isdigit()==True):#valido que el argumento actual sea un valor numerico
			if int(sys.argv[i]) in ventas.values():#verifico si el valor se encuentra en los valores de la lista
				ventasInv = {v: k for k, v in ventas.items()}#invierto la lista para que las claves sean valores y viceversa
				print(ventasInv[int(sys.argv[i])])#acceso directo a lo que originalmente era una clave
			else:
				print("No encontrado")
		else:
			print(sys.argv[i]," es un argumento invalido")
else:
	print("sin argumentos")