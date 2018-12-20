from Diccionario import ventas
#trimestres

def getValores(diccionario=ventas):
	q1,q2,q3,q4=0,0,0,0
	q1=diccionario.get("Enero")+diccionario.get("Febrero")+diccionario.get("Marzo")
	q2=diccionario.get("Abril")+diccionario.get("Mayo")+diccionario.get("Junio")
	q3=diccionario.get("Julio")+diccionario.get("Agosto")+diccionario.get("Septiembre")
	q4=diccionario.get("Octubre")+diccionario.get("Noviembre")+diccionario.get("Diciembre")
	return (q1,q2,q3,q4)
print(getValores())
	