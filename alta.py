import commands
import sys
import os
#pedimos el nombre
nombre = raw_input("introduce el nombre: ")

#vemos si el usuario existe buscamos el nombre en la carpeta que se llamara 
#como el nombre de dominio
os.system("ls /home/sergio/pruebahosting > usuarios.txt")
#el fichero se crea donde ejecutamos el programa
f=open("/home/sergio/hosting/usuarios.txt","r")
fichero=f.readlines()
f.close()
print fichero
print fichero[0]
#for linea in fichero:
#	print linea
#	if nombre==linea:
#		print "nombre existente"
#print carpetas

