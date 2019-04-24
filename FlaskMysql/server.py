from Conexion import Conexion
link=Conexion("localhost","root","avaras08","3306")
link.setDataBase("Prueba3")
link.createTable("Personas","Prueba3")
