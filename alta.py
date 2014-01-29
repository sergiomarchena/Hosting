import os
import MySQLdb
#pedimos el nombre
nombre = str(raw_input("introduce el nombre: "))
dominio = raw_input("introduce el nombre de dominio: ")
#abrimos una conexion
base = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="usuarios")
cursor=base.cursor()
#vemos si el usuario existe buscamos en mysql el nombre de usuario
consultausuario="select nombre from usuarios where nombre='%s';" %nombre
cursor.execute(consultausuario)
consulta_usuario = cursor.fetchone()
if consulta_usuario !=None:
	print "nombre de usuario existente"
	sys.exit
else:
#vemos si existe el dominio que tambien lo guardaremos en mysql
	consultadominio="select dominio from usuarios where dominio='%s';" %dominio
	cursor.execute(consultadominio)
	consulta_dominio = cursor.fetchone()
	if consulta_dominio !=None:
		print "nombre de dominio existente"
		sys.exit
	else:
#creamos el directorio personal y le anyadimos el index.html
		os.system("mkdir /home/sergio/pruebahosting/%s" %nombre)
		os.system("cp /home/sergio/plantillas_hosting/index.html /home/sergio/pruebahosting/%s"%nombre)
#crearemos el nuevo virtualhost
		virtual_host="/home/sergio/plantillas_hosting/virtual_host"
		virtual=open(virtual_host, "r")
		filew = open(virtual_host+'.mod', "w")
		buff = virtual.read()
		char1='%nombre%'
		rbuff = buff.replace(char1, nombre)
		filew.write(rbuff)
		virtual.close()
		filew.close()
#esto crea un fichero llamado virtual_host.mod le cambiamos el nombre y movemos a apache
		os.system("mv /home/sergio/plantillas_hosting/virtual_host.mod /etc/apache2/sites-available/%s"%nombre)
#activamos el modulo y reiniciamos apache
		os.system("a2ensite %s"%nombre)
		os.system("service apache2 restart")
