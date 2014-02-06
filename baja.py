import MySQLdb
import sys
#pedimos el nombre
dominio = raw_input("introduce el nombre de dominio: ")
cortacadena=dominio.split(".")
nombre=cortacadena[0]
#abrimos una conexion
base = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="ftpd")
cursor=base.cursor()
#vemos si el usuario existe buscamos en mysql el nombre de usuario
consultausuario="select ndominio from usuarios where ndominio='%s';" %dominio
cursor.execute(consultausuario)
#consulta_usuario = cursor.fetchone()
if consultausuario == None:
	print "El usuario %s no existe"%nombre
	sys.exit
else:
#borramos la carpeta personal
	os.system("rm -r /srv/www/%s" % nombre)
#desabilitamos los virtualhost
	os.system("a2dissite www.%s>/dev/null"%dominio)
        os.system("a2dissite mysql.%s>/dev/null"%dominio)
#borramos los virtualhosts
	os.system("rm -r /etc/apache2/sites-available/www.%s"%dominio)
	os.system("rm -r /etc/apache2/sites-available/mysql.%s"%dominio)
#reiniciamos apache
	os.system("service apache2 restart>/dev/null")
#borramos el usuario de mysql y las bases de datos
	borrarbases="drop database my%s"%nombre
	cursor.execute(borrarbases)
	base.commit()
	borrausuario=" drop user my%s@localhost" %nombre 
    	cursor.execute(borrausuario)
    	base.commit()
#borramos la columna de la tabla ftpd
	borracolumna="delete from usuarios where ndominio='%s';" %nombre
    	cursor.execute(borracolumna)
   	base.commit()
#borramos el fichero db. donde 
	os.system("rm -r /etc/bind/%s" %dominio)
#borramos la zona


