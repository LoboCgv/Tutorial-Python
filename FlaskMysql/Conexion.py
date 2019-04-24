import mysql.connector

class Conexion:
	
	mydb=None#atributo con la conexion a la base de datos
	mycursor=None
	def __init__(self,host,user,passwd,port):
		self.mydb = mysql.connector.connect(
			host=host,
			user=user,
			passwd=passwd,
			port=port,
			)
		self.mycursor=self.mydb.cursor()
	def getConect():
		return self.mydb
	def setDataBase(self,database):
		self.mycursor.execute("create database "+ database)
	def createTable(self,nombreTabla,database):
		self.mycursor.execute("use "+database)
		self.mycursor.execute("create table "+nombreTabla+" (rut varchar(15),nombre varchar(40),edad int(11))")
		self.mycursor.execute("alter table "+nombreTabla+" add column id int auto_increment primary key")
		self.mycursor.execute("show tables")
		for x in self.mycursor:
			print(x)
	
		