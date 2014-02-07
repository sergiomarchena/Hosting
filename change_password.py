import MySQLdb
import sys
import getpass
import sys
accion=(sys.argv[1])
base = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="mysql")
cursor=base.cursor()
#si la accion pedida es mysql
if accion == "mysql":
	print "procederemos a cambiar la contrasenna de mysql"
#pedimos el usuario para el que vamos a cambiar la contrasenna y la contrasenna antigua
	usuariomysql=(sys.argv[2])
	contrasenaantigua=(sys.argv[3])
#codificamos la contrasenna igual que en mysql
	base2 = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="cambiocontrasenna")
	cursor2=base2.cursor()
#insertamos en una tabla diferente la contrasenna encriptada
	usercontra="insert into contrasenna values('"+usuariomysql+"',PASSWORD('"+contrasenaantigua+"'));"
	cursor2.execute(usercontra)
        base2.commit()
#buscamos la contrasenna codificada y mas tarde la comparamos con la de la otra tabla
	contrasennacodificada="select contrasenna from contrasenna;"
        cursor2.execute(contrasennacodificada)
        consultacodificada = cursor2.fetchone()
	base2.close() 
#buscamos si existe el usuario
	consultausuario="select user from user where user='"+usuariomysql+"';"
	cursor.execute(consultausuario)
	consulta_usuario = cursor.fetchone()
#buscamos si es la misma contrasenna
	consultacontrasenna="select password from user where user='"+usuariomysql+"';"
        cursor.execute(consultacontrasenna)
        consulta_contrasenna = cursor.fetchone()
#si la contrasenna y el usuario coinciden procedemos a cambiarla
	if consulta_usuario[0]== usuariomysql and consulta_contrasenna[0]== consultacodificada[0]:
		print "usuario y contrasenna correctas"
#contrasenna nueva
		contrasenanueva=(sys.argv[4])
		cambio="SET PASSWORD FOR "+usuariomysql+"@localhost = PASSWORD('"+contrasenanueva+"');"
		cursor.execute(cambio)
		base.commit()
		print "contrasenna actualizada correctamente"
#borramos el registro creado para que la tabla no aumente
			base2 = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="cambiocontrasenna")
        		cursor2=base2.cursor()
			borrarregistro="delete from contrasenna;"
			cursor2.execute(borrarregistro)
        		base2.commit()
			base2.close()
		else:
			print "contrasena nueva incorrecta"
	else:
		print "contrasenna incorrecta"
#tambien borraremos la tabla porque si no el usuario se quedaria guardado y en la siguiente consulta apareceria 2 veces
 		base2 = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="cambiocontrasenna")
                cursor2=base2.cursor()
                borrarregistro="delete from contrasenna;"
                cursor2.execute(borrarregistro)
                base2.commit()
                base2.close()
		sys.exit	 	

elif accion == "ftp":
	base3 = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="ftpd")
	cursor3=base3.cursor()
	print "procederemos a cambiar la contrasenna de ftp"
#vemos el usuario para el que vamos a cambiar la contrasenna y la contrasenna antigua
        usuarioftp=(sys.argv[2])
        contrasenaantigua=(sys.argv[3])
#codificamos la contrasenna igual que en la contrasenna se guarda en la tabla ftpd
        base2 = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="cambiocontrasenna")
        cursor2=base2.cursor()
#insertamos en una tabla diferente la contrasenna encriptada
        usercontra="insert into contrasenna values('"+usuarioftp+"',PASSWORD('"+contrasenaantigua+"'));"
        cursor2.execute(usercontra)
        base2.commit()
#buscamos la contrasenna codificada y mas tarde la comparamos con la de la otra tabla
        contrasennacodificada="select contrasenna from contrasenna;"
        cursor2.execute(contrasennacodificada)
        consultacodificada = cursor2.fetchone()
        base2.close()
#buscamos si existe el usuario
        consultausuario="select username from usuarios where username='"+usuarioftp+"';"
        cursor3.execute(consultausuario)
        consulta_usuario = cursor3.fetchone()
#buscamos si es la misma contrasenna
        consultacontrasenna="select password from usuarios where username='"+usuarioftp+"';"
        cursor3.execute(consultacontrasenna)
        consulta_contrasenna = cursor3.fetchone()
#si la contrasenna y el usuario coinciden procedemos a cambiarla
        if consulta_usuario[0]== usuarioftp and consulta_contrasenna[0]== consultacodificada[0]:
                print "usuario y contrasenna correctas"
# contrasenna nueva
                contrasenanueva=(sys.arg[4])
                if contrasenanueva == pruebadenuevo:
                        cambio="update usuarios set password = PASSWORD('"+contrasenanueva+"')where username='"+usuarioftp+"';"
                        cursor3.execute(cambio)
                        base3.commit()
                        print "contrasenna actualizada correctamente"
#borramos el registro creado para que la tabla no aumente
                        base2 = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="cambiocontrasenna")
                        cursor2=base2.cursor()
                        borrarregistro="delete from contrasenna;"
                        cursor2.execute(borrarregistro)
                        base2.commit()
                        base2.close()
                else:
                        print "contrasena nueva incorrecta"
        else:
                print "contrasenna incorrecta"
#tambien borraremos la tabla porque si no el usuario se quedaria guardado y en la siguiente consulta apareceria 2 veces
 		base2 = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="cambiocontrasenna")
                cursor2=base2.cursor()
                borrarregistro="delete from contrasenna;"
                cursor2.execute(borrarregistro)
                base2.commit()
                base2.close()
                sys.exit
	
else:
	print "si introduce mysql como primer parametro cambiara la contrasenna de el usuario mysql ademas como segundo el usuario,tercer parametro la contrasenna antigua y como cuarto la nueva contrasenna o puede introducir ftp para cambiar la de el usuario ftp y los parametros usuario, antigua y nueva"
 
