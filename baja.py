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
if consulta_usuario == None:
	print "El usuario %s no existe"%nombre
	sys.exit
else:
#borramos la carpeta personal
	os.system("rm -r /srv/www/%s" % nombre)
	os.system("a2dissite %s > /dev/null" % nombre)
    	
