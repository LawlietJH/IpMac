# -*- Coding: utf-8 -*-
# Python 3
# By: LawlietJH
# IpMac
# Versión: 1.0.1

import os

Autor = "LawlietJH"
Version = "v1.0.1"

def Chk_Dep():
	
	try:
		import psutil
		
	except ModuleNotFoundError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("Title Instalando psutil && pip install psutil > Nul && cls && Title IpMac.py            By: LawlietJH")
		
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.

Chk_Dep()				#~ Se instala el módulo pytube si esta no esta instalada.
import psutil 		#~ Se importa la módulo.



Lista = []
Datos = psutil.net_if_addrs()
cont = 0

for x in Datos:
	
	cont += 1
	print(" [*] ", cont, " - ", x)
	Lista.append(x)

xD = int(input("\n\n\t Opciones de Busqueda: "))

Datos = Datos.pop(Lista[xD-1]) # Sacamos los datos de la red Elegida.

print("\n\n\n MAC:\t" + str(Datos[0][1]))
print("\n IPv4:\t" + str(Datos[1][1]))

os.system("Pause > Nul")
