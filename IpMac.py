# -*- Coding: utf-8 -*-
# Python 3
# By: LawlietJH
# IpMac
# Versión: 1.0.5



import os

Autor = "LawlietJH"
Version = "v1.0.5"



#=======================================================================



def Chk_Dep():	# Se Instalan las Dependencias.

	try:
		import psutil
		
	except ModuleNotFoundError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("Title Instalando psutil && pip install psutil > Nul"+\
				  "&& cls && Title IpMac.py            By: LawlietJH")
		
	except Exception as ex:				# Ver cuando ocurre un error y poder añadirlo
		print( type(ex).__name__ )		# A las ecepciones, y no cierre el programa.



Chk_Dep()			# Se instala el módulo psutil si esta no esta instalada.
import psutil 		# Se importa la módulo.



#=======================================================================



def getMAC(Datos):	# Devuelve La Direción MAC.
	
	MAC = str(Datos[0][1])
	
	return MAC



def getIPv4(Datos):	# Devuelve La IPv4
	
	IPv4 = str(Datos[1][1])
	
	return IPv4



def getAdaptadores():	# Se Obtiene Una Lista Con Todos Los Nombres de Adaptadores Disponibles.
	
	Info = psutil.net_if_addrs()
	
	Adaptadores = []
	
	for xD in Info:
		
		Adaptadores.append(xD)
		
	return Adaptadores


#=======================================================================



def Main():	# Función Principal.
	
	Datos =  psutil.net_if_addrs()
	Adaptadores = getAdaptadores()
	cont = 0
	
	for xD in Adaptadores:
		
		cont += 1
		print(" [*] ", cont, " - ", xD)
	
	print("\n [*]  0 - Salir...")
	
	try:
		xD = input("\n\n\t Opciones de Busqueda: ")
	except:
		print("\n\n\t [!] Opción No Válida.")
		
	if xD == "0": exit(1)
	elif xD == "": exit(1)
	else: xD = int(xD)
	
	Adaptador = Datos.pop(Adaptadores[xD-1]) # Sacamos los datos de la red Elegida.
	
	MAC = getMAC(Adaptador)
	IPv4 = getIPv4(Adaptador)
	
	print("\n\n\n MAC:\t" + MAC)
	print("\n IPv4:\t" + IPv4)



#=======================================================================


if __name__ == "__main__":
	
	os.system("cls && Title IpMac.py            By: LawlietJH")
	
	Main()
	
	os.system("Pause > Nul")
