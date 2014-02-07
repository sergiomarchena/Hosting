import os
import MySQLdb
import string
from random import choice
import sys
#pedimos el nombre
nombre = (sys.argv[1])
dominio = (sys.argv[2])
#abrimos una conexion
base = MySQLdb.connect(host="localhost", user="root", passwd="sergio", db="ftpd")
cursor=base.cursor()
#vemos si el usuario existe buscamos en mysql el nombre de usuario
consultausuario="select username from usuarios where username='%s';" %nombre
cursor.execute(consultausuario)
consulta_usuario = cursor.fetchone()
if consulta_usuario !=None:
        print "nombre de usuario existente"
        sys.exit
else:
#vemos si existe el dominio que tambien lo guardaremos en mysql
        consultadominio="select ndominio from usuarios where ndominio='%s';" %dominio
        cursor.execute(consultadominio)
        consulta_dominio = cursor.fetchone()
        if consulta_dominio !=None:
                print "nombre de dominio existente"
                sys.exit
        else:
#creamos el directorio personal y le anyadimos el index.html    
                os.system("mkdir /srv/www/%s" %nombre)
                os.system("cp /home/debian/plantillas_hosting/index.html /srv/www/%s"%nombre)
#crearemos el nuevo virtualhost
 virtual_host="/home/debian/plantillas_hosting/virtual_host"
                virtual=open(virtual_host, "r")
                filew = open(virtual_host+'.mod', "w")
                buff = virtual.read()
                char1='%nombre%'
                rbuff = buff.replace(char1, nombre)
                filew.write(rbuff)
                virtual.close()
                filew.close()
#esto crea un fichero llamado virtual_host.mod le cambiamos el nombre y movemos a apache
                os.system("mv /home/debian/plantillas_hosting/virtual_host.mod /etc/apache2/sites-available/www.%s"%dominio)
#copiar virtual_host de mysql
                mysql_virtual_host="/home/debian/plantillas_hosting/mysql_virtual_host"
                mysql_virtual=open(mysql_virtual_host, "r")
                filew = open(mysql_virtual_host+'.mod', "w")
                buff = mysql_virtual.read()
                char1='%dominio%'
                rbuff = buff.replace(char1, dominio)
                filew.write(rbuff)
                mysql_virtual.close()
                filew.close()
#esto crea un fichero llamado mysql_virtual_host.mod le cambiamos el nombre y movemos a apache
                os.system("mv /home/debian/plantillas_hosting/mysql_virtual_host.mod /etc/apache2/sites-available/mysql.%s"%dominio)
#activamos el modulo y reiniciamos apache
                activar=os.system("a2ensite www.%s>/dev/null"%dominio)
		activarmysql=os.system("a2ensite mysql.%s>/dev/null"%dominio)
                reiniciar=os.system("service apache2 restart>/dev/null")
#creamos un nuevo usuario para ftp
#generamos una contrasenya aleatoria
               def GenPasswd(n):
                        return ''.join([choice(string.letters + string.digits) for i in range(n)])
                contrasenna=GenPasswd(8)
                print"esta es tu contrasenna para el usuario ftp:", contrasenna
#insertamos el usuario en mysql
                consultauid="select max(uid) from usuarios;"
                cursor.execute(consultauid)
                consulta_uid = cursor.fetchone()
#si la tabla esta vacia introduce el 5001
                if consulta_uid[0] == None:
                        conuid=str("5001")
                        usermysql="insert into usuarios values('"+ nombre+"'," +"PASSWORD('"+contrasenna+"'),"+conuid+","+conuid+","+"'/srv/www/"+nombre+"',"+"'/bin/false1',"+"1,'"+dominio+"');"
			cursor.execute(usermysql)
                        base.commit()
                        print "El proceso se realizo satisfactoriamente"
#en caso contrario le suma uno al numero maximo de la tabla
                else:
                        conuid=consulta_uid[0]+1
                        conuidn=str(conuid)
                        usermysql="insert into usuarios values('"+ nombre+"'," +"PASSWORD('"+contrasenna+"'),"+conuidn+","+conuidn+","+"'/srv/www/"+nombre+"',"+"'/bin/false1',"+"1,'"+dominio+"');"
			cursor.execute(usermysql)
                        base.commit()
                        print "El usuario ftp se ha creado correctamente"
#introducimos un usuario en mysql
#volvemos a generar otra contrasenna
                def GenPasswd(n):
                        return ''.join([choice(string.letters + string.digits) for i in range(n)])
                contrasennamysql=GenPasswd(8)
                print "esta es tu contrasenna para tu usuario mysql:",contrasennamysql
#creamos la base de datos y le damos permisos
		basededatos="CREATE DATABASE "+nombre
                cursor.execute(basededatos)
                base.commit()
#creamos el usuario y le damos permisos
                usuariomysql="GRANT ALL ON "+nombre+".* TO my"+nombre+"@localhost IDENTIFIED BY '"+contrasennamysql+"'";
                cursor.execute(usuariomysql)
                base.commit()
                print "la base de datos y el usuario mysql han sido creado correctamente"
#creamos la nueva zona
		fichzona="/home/debian/plantillas_hosting/zona"
                zonadom=open(fichzona,"r")
                wzona = open(fichzona+'.mod', "w")
                zonabuff = zonadom.read()
                char1='%dominio%'
                cambio = zonabuff.replace(char1, dominio)
                wzona.write(cambio)
                zonadom.close()
                wzona.close()
#abrimos el fichero modificado y modificamos el named.conf.local
                ficheromodificado=open("/home/debian/plantillas_hosting/zona.mod","r")
                ficheromodificado1=ficheromodificado.read()
                g=open("/etc/bind/named.conf.local","a")
                g.write(ficheromodificado1)
                g.close()
                os.system("rm -r /home/debian/plantillas_hosting/zona.mod")
#creamos el nuevo fichero de dominio
		ficherodominio="/home/debian/plantillas_hosting/db.plantilla"
                domain=open(ficherodominio, "r")
                filew = open(ficherodominio+'.mod', "w")
                buff = domain.read()
                variable1='%dominio%'
                rbuff = buff.replace(variable1, dominio)
                filew.write(rbuff)
                domain.close()
                filew.close()
#cambiamos de lugar y nombre
                os.system("mv /home/debian/plantillas_hosting/db.plantilla.mod /etc/bind/db.%s"%dominio)
#reiniciamos bind
                reiniciar=os.system("service bind9 restart>/dev/null")

