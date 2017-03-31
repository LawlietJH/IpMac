# -*- Coding: utf-8 -*-
# Python 3
# By: LawlietJH
# IpMac
# Versión: 1.0.9



import time
import os



Autor = "LawlietJH"
Version = "v1.0.9"



#=======================================================================



def Salir(Num=0):
	
	try:
		time.sleep(1.5)
		exit(Num)
	except KeyboardInterrupt:
		Salir(Num)



def Chk_Dep():	# Se Instalan las Dependencias.

	try:
		import psutil
		
	except ModuleNotFoundError:
		print("\n\n\t\t [!] Instalando Dependencias...\n\n\t\t")
		os.system("Title Instalando psutil && pip install psutil > Nul"+\
				 "&& cls && Title IpMac.py                 By: LawlietJH")
		
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



def getDatos():
	
	Datos =  psutil.net_if_addrs()
	
	return Datos



def getAdaptadores():	# Se Obtiene Una Lista Con Todos Los Nombres de Adaptadores Disponibles.
	
	Info = psutil.net_if_addrs()
	
	Adaptadores = []
	
	for xD in Info:	Adaptadores.append(xD)
		
	return Adaptadores



def ImprimeLista(Adaptadores):
	
	global cont
	cont = 1
	
	print("\n\n\n")
	
	for xD in Adaptadores:
		print("\t [*] ", cont, " - ", xD)
		cont += 1
	
	print("\n\t [*]  0 - Salir...")
	
	try:
		xD = input("\n\n\t [+] Elige Una Opción: ")
	except KeyboardInterrupt:
		print("\n\n\t\t [!] Saliendo...")
		Salir(1)
	except:
		print("\n\n\t\t [!] Opción No Válida.")
	
	if xD == "0":	exit(1)
	elif xD == "":	return xD
	else:
		try:
			return int(xD)
		except:
			xD = False
			return xD



#=======================================================================



def Main():	# Función Principal.
	
	global cont
	
	Datos = getDatos()				# Obtenemos La Información de Todos Los Adaptadores de Red.
	Adaptadores = getAdaptadores()	# Obtenemos Todos Los Nombres De Los Adaptadores Disponibles.
	
	xD = ImprimeLista(Adaptadores)	# Imprime La Lista Con Los Nombres De Los Adaptadores.
	
	if xD == "":
		print("\n\n\t\t [!] Elige Una Opción!"), time.sleep(1.5)
		return
		
	elif xD > cont:
		print("\n\n\t\t [!] Opción No Inexistente!"), time.sleep(1.5)
		return
		
	elif xD == False:
		print("\n\n\t\t [!] Caracteres No Válido!"), time.sleep(1.5)
		return
		
	Adaptador = Datos.pop(Adaptadores[xD-1]) # Sacamos Los Datos Del adaptador De Red Seleccionado.
	
	MAC = getMAC(Adaptador)			# Obtenemos La MAC Del Adaptador Seleccionado.
	IPv4 = getIPv4(Adaptador)		# Obtenemos La IPv4 Del Adaptador Seleccionado.
	
	print("\n\n\n\t\t [*] MAC:\t" + MAC)
	print("\n\t\t [*] IPv4:\t" + IPv4 + "\n\n\n")
	
	os.system("Pause > Nul")



#=======================================================================



cont = 0



#=======================================================================



if __name__ == "__main__":
	
	while True: 
		
		os.system("cls && Title IpMac.py                 By: LawlietJH")
		
		Main()


