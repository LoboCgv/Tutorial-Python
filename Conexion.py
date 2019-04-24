import mysql.connector
#python -m pip install mysql-connector
mydb = mysql.connector.connect(
  host="localhost",
  user="carlos",
  passwd="",
  port="3307",
  #si conocemos la base de datos ponemos aca
  database="bdpython"
)

'''mycursor=mydb.cursor()
mycursor.execute("create database bdpython")
mycursor.execute("show databases")
for x in mycursor:
	print(x)
#print(mydb)'''
#la idea es que cada cursor sea trabajado con consultas mysql normales
mycursor=mydb.cursor()
#mycursor.execute("create table personas(rut varchar(15),nombre varchar(40),edad int(11))")
#mycursor.execute("alter table personas add column id int auto_increment primary key")
#mycursor.execute("show tables")
#for x in mycursor:
#	print(x)
mycursor=mydb.cursor()
#consulta="insert into personas (rut,nombre,edad) values(%s,%s,%s)"
#val=("150695929","Carlos","36")
#mycursor.execute(consulta,val)
#mydb.commit()
#print(mycursor.rowcount,"datas")
#insertar varios
'''consulta="insert into personas (rut,nombre,edad) values(%s,%s,%s)"
val=[
("rut abarzua","Carlos","53"),
("rut cote","Cote","32"),
("rut bombon","Bombon","34")
]

mycursor.executemany(consulta,val)
mydb.commit()
print(mycursor.rowcount,"datas")'''
#select
mycursor.execute("select * from personas")
myresult=mycursor.fetchall()#lista de tuplas
#creo lista
lista=[]
for x in myresult:
	#creo diccionario
	actual={'nombre':x[1],'edad':x[2]}
	print(actual)
	lista.append(actual)
print(lista)


#mycursor.execute("select nombre,edad from personas")
#myresult=mycursor.fetchall()#lista de tuplas
#for x in myresult:
#	print(x)
#print(myresult[0][1])#obtengo un rut

#mycursor.execute("select nombre,edad from personas where nombre='carlos'")
#myresult=mycursor.fetchone()#lista de tuplas
#print(myresult)

#where
#mycursor.execute("select * from personas where nombre='carlos'")
#myresult=mycursor.fetchall()#lista de tuplas
#for x in myresult:
#	print(x)
#print(myresult[0][1])#obtengo un rut

#convertir lista en diccionario
