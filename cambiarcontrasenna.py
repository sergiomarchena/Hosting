import MySQLdb
print "si introduce mysql cambiara la contrasenna de el usuario mysql o puede introducir ftp para cambiar la de el usuario ftp"
accion=raw_input("escriba su operacion a realizar: ")
base = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="mysql")
cursor=base.cursor()
#si la accion pedida es mysql
if accion == "mysql":
	print "procederemos a cambiar la contrasenna de mysql"
#pedimos el usuario para el que vamos a cambiar la contrasenna y la contrasenna antigua
	usuariomysql=raw_input("introduzca su usuario mysql: ")
	contrasenaantigua=raw_input("introduzca su contrasenna antigua mysql: ")
#codificamos la contrasenna igual que en mysql
	contrasennacodificada= 
#buscamos si existe el usuario
	consultausuario="select user from user where user='"+usuariomysql+"';"
	cursor.execute(consultausuario)
	consulta_usuario = cursor.fetchone()
#buscamos si es la misma contrasenna
	consultacontrasenna="select password from user where user='"+usuariomysql+"';"
        cursor.execute(consultacontrasenna)
        consulta_contrasenna = cursor.fetchone()
#si la contrasenna y el usuario coinciden procedemos a cambiarla
	if consulta_usuario[0]== usuariomysql and consulta_contrasenna[0]=consultacontrasenna:
		print "usuario y contrasenna correctas"
	else:
		print "contrasenna incorrecta"
	 	
elif accion == "ftp":
	print "procederemos a cambiar la contrasenna de ftp"
	usuarioftp=raw_input("introduzca su usuario ftp: ")
	contrasenaantigua=raw_input("introduzca su contrasenna antigua ftp: ")
	
else:
	print "opcion",accion,"incorrecta introduzca fpt o mysql"
