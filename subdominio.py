import os
import sys

nombre=(sys.argv[1])
subdominio=(sys.argv[2])

import MySQLdb
base = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="ftpd")
cursor = base.cursor()
consulta = "select ndominio from usuarios where username='%s';" % (nombre)
cursor.execute(consulta)
resultado = cursor.fetchone()
if resultado == None:
    print "Lo sentimos, el usuario %s no exite" % (nombre)
else:
#creamos la capeta del subdominio
    	os.system("mkdir /srv/www/%s/subdominio" % (nombre))
#creamos la carpeta con el nombre del subdominio
    	os.system("mkdir /srv/www/%s/subdominio/%s" % (nombre,subdominio))
#creamos el fichero de ejemplo    
    	os.system("echo Pagina de %s en construccion  > /srv/www/%s/subdominio/%s/index.html" %(nombre,nombre,subdominio))
#modificamos el fichero virtualhost creado nuevo y modificamos el primer parametro    
    	virtual_host="/home/debian/plantillas_hosting/virtual_hostsubdominio"
	virtual=open(virtual_host, "r")
    	filew = open(virtual_host+'.mod', "w")
    	buff = virtual.read()
    	char1='%nombre%'
    	rbuff = buff.replace(char1, nombre)
    	filew.write(rbuff)
    	virtual.close()
    	filew.close()
#modificamos el fichero modificado otra vez para el dominio
    	virtual_host="/home/debian/plantillas_hosting/virtual_hostsubdominio.mod"
    	virtual=open(virtual_host, "r")
    	filew = open(virtual_host+'.mod', "w")
    	buff = virtual.read()
    	char1='%subdominio%'
    	rbuff = buff.replace(char1, subdominio)
    	filew.write(rbuff)
    	virtual.close()
    	filew.close()
#borramos el primer fichero modificado que se ha creado 
    	os.system("rm -r /home/debian/plantillas_hosting/virtual_hostsubdominio.mod")
#movemos el fichero a apache
    	os.system("mv /home/debian/plantillas_hosting/virtual_hostsubdominio.mod.mod /etc/apache2/sites-available/%s"%subdominio)
#activamos el dominio
    	os.system("a2ensite %s>/dev/null" % subdominio)
    	os.system("service apache2 restart>/dev/null ")
#añadimos la resolucion directa
    	directa = open("/etc/bind/db.%s.com" % nombre,"a")
    	directa.write("%s  CNAME s1\n" % subdominio)
    	directa.close()
    	os.system("service bind9 restart>/dev/null ")
#annadimos un alias al host principal para que no pueda entrar /subdominio/subdominio
    	db = open("/etc/apache2/sites-available/www.%s.com" % nombre,"a")
 	db.write("Alias /subdominio/%s/ \"/usr/share/apache2/error/HTTP_NOT_FOUND.html.var\" "%subdominio)
	db.close()
        os.system("service apache2 restart >/dev/null")
        print "El subdominio fue creado correctamente"

