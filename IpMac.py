# -*- Coding: utf-8 -*-
# Python 3
#
#                    ██╗██████╗ ███╗   ███╗ █████╗  ██████╗
#                    ██║██╔══██╗████╗ ████║██╔══██╗██╔════╝
#                    ██║██████╔╝██╔████╔██║███████║██║     
#                    ██║██╔═══╝ ██║╚██╔╝██║██╔══██║██║     
#                    ██║██║     ██║ ╚═╝ ██║██║  ██║╚██████╗
#                    ╚═╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝
#                                                         By: LawlietJH
#                                                               v1.1.8

import datetime
import locale
import time
import os



Version = "v1.1.8"



# Banners: http://patorjk.com/software/taag/



Banner1 = """
                     ██╗██████╗ ███╗   ███╗ █████╗  ██████╗
                     ██║██╔══██╗████╗ ████║██╔══██╗██╔════╝
                     ██║██████╔╝██╔████╔██║███████║██║     
                     ██║██╔═══╝ ██║╚██╔╝██║██╔══██║██║     
                     ██║██║     ██║ ╚═╝ ██║██║  ██║╚██████╗
                     ╚═╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝
"""
# Fuente: ANSI Shadow - http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=IpMac


Banner2 = """
                                  ╦┌─┐╔╦╗┌─┐┌─┐
                                  ║├─┘║║║├─┤│  
                                  ╩┴  ╩ ╩┴ ┴└─┘
"""
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=IpMac

Autor = """
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩
"""
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH



#=======================================================================



cont = 0
VIPv4 = False
VIPv6 = False



#=======================================================================



def Dat():	# Función Que Permite Mostrar Los Datos Del Script.
	
	os.system("cls && Title IpMac.py                "+\
			"By: LawlietJH                "+Version+"    ")
	print("\n\n", Banner1)
	print("\n\n", Autor)
	print("\n{:^80}".format(Version))
	
	time.sleep(2)
	

def Salir(Num=0):	# Fucnión Que Permite Salir Del Script Sin Error Alguno.
	
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



Chk_Dep()			# Se instala el módulo psutil si este no esta instalado.
try:
	import psutil 		# Se Importa El Módulo.
except:					# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
	print("\n\n   No se pudo instalar correctamente el Módulo 'psutil'.")
	print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
	print("\n\t 'pip install psutil'   o   ' pip3 install psutil'")
	
	try:
		os.system("Pause > Nul")
	except KeyboardInterrupt: pass
	
	Dat()
	Salir(0)


#=======================================================================



def getMAC(Adaptador):	# Devuelve La Direción MAC De Los Adaptadores De Red.
	
	MAC = ""
	
	if "AF_LINK" in str(Adaptador[0][0]):
	
		MAC = str(Adaptador[0][1])
		MAC = MAC.replace("-",":")
		
	elif "AF_LINK" in str(Adaptador[1][0]):
	
		MAC = str(Adaptador[1][1])
		MAC = MAC.replace("-",":")
	
	return MAC



def getIP(Adaptador):	# Devuelve La IP Ya Sea Versión 4 y/o 6.
	
	global VIPv4
	global VIPv6
	VIPv4 = False
	VIPv6 = False
	IPv4 = " "
	IPv6 = " "
	
	
	try:
		if "AF_INET6" in str(Adaptador[0][0]):
			VIPv6 = True
			IPv6 = str(Adaptador[0][1])
			return (IPv4, IPv6)
		elif "AF_INET" in str(Adaptador[0][0]):
			VIPv4 = True
			IPv4 = str(Adaptador[0][1])
			
		if "AF_INET6" in str(Adaptador[1][0]):
			VIPv6 = True
			IPv6 = str(Adaptador[1][1])
			return (IPv4, IPv6)
		elif "AF_INET" in str(Adaptador[1][0]):
			VIPv4 = True
			IPv4 = str(Adaptador[1][1])
		
		if "AF_INET6" in str(Adaptador[2][0]):
			VIPv6 = True
			IPv6 = str(Adaptador[2][1])
			return (IPv4, IPv6)
		elif "AF_INET" in str(Adaptador[2][0]):
			VIPv4 = True
			IPv4 = str(Adaptador[2][1])
			
	except:
		print("Error")
	
	return(IPv4, IPv6)


def getDatos():	# Devuelve Todos Los Datos Sobre Todos Los Adaptadores De Red Disponibles.
	
	Datos =  psutil.net_if_addrs()
	
	return Datos



def getAdaptadores():	# Se Obtiene Una Lista Con Todos Los Nombres de Adaptadores Disponibles.
	
	Info = psutil.net_if_addrs()
	
	Adaptadores = []
	
	for xD in Info:	Adaptadores.append(xD)
		
	return Adaptadores



def ImprimeLista(Adaptadores):	#Imprime Los Nombres De Los Adaptadores De red Disponibles.
	
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
		try:
			time.sleep(1)
		except KeyboardInterrupt: pass
		Dat()
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



def ChkDatos():
	
	Eny = open("Logs.ZioN","r+")
	
	Comando = "echo %UserName%"
	Usuario = os.popen(Comando)
	Usuario = Usuario.read()
	
	Lineas = Eny.readlines()

	if Lineas == []: Eny.write("\n\t     [+] Por: LawlietJH - IpMac "+Version)
	if not " |||||||||||||||| [+] Logs del Usuario: " + Usuario in Lineas:
		
		Eny.write("\n\n ================================================================="+\
				  "\n _________________________________________________________________"+\
				  "\n\n\n |||||||||||||||| [+] Logs del Usuario: " + Usuario +\
				  "\n _________________________________________________________________")			  
	Eny.close()



#=======================================================================



def Main():	# Función Principal.
	
	global VIPv4
	global VIPv6
	global cont
	
	
	dt = datetime.datetime.now()
	FH = dt.strftime("\n\n\n\t  +  %A %d de %B del %Y - %H:%M").title()
	print(FH)
	
	Log = open("Logs.ZioN","a")
	
	ChkDatos()
	
	Datos = getDatos()				# Obtenemos La Información de Todos Los Adaptadores de Red.
	Adaptadores = getAdaptadores()	# Obtenemos Todos Los Nombres De Los Adaptadores Disponibles.
	
	xD = ImprimeLista(Adaptadores)	# Imprime La Lista Con Los Nombres De Los Adaptadores.
	
	if xD == "":
		print("\n\n\t\t [!] Elige Una Opción!"), time.sleep(1.5)
		return
	elif xD >= cont:
		print("\n\n\t\t [!] Opción Inexistente!"), time.sleep(1.5)
		return
	elif xD == False:
		print("\n\n\t\t [!] Caracteres No Válido!"), time.sleep(1.5)
		return
	
	
	FH = dt.strftime("\t%A %d de %B del %Y - %H:%M").title()
	Log.write("\n\n ================================================================="+\
	          "\n\n [+] Fecha Y Hora: " + FH + "\n\n [+] Interfaz '" + Adaptadores[xD-1] + "':\n")
	
	
	Adaptador = Datos.pop(Adaptadores[xD-1]) # Sacamos Los Datos Del adaptador De Red Seleccionado.
	
	MAC = getMAC(Adaptador)			# Obtenemos La MAC Del Adaptador Seleccionado.
	IPv4, IPv6 = getIP(Adaptador)	# Obtenemos La IP Del Adaptador Seleccionado.
	
	print("\n\n\n\t\t [*] MAC:\t" + MAC)		# Imprime La Dirección MAC.
	Log.write("\n\t [*] MAC:\t" + MAC)
	
	if len(Adaptador) == 4:						# Si Hay Más de Una IPv4.
		print("\n\t\t [*] IPv4 (1):\t" + Adaptador[1][1])
		print("\n\t\t [*] IPv4 (2):\t" + Adaptador[2][1])
		print("\n\t\t [*] IPv6:\t" + Adaptador[3][1])
		
		Log.write("\n\t [*] IPv4 (1):\t" + Adaptador[1][1] +\
				  "\n\t [*] IPv4 (2):\t" + Adaptador[2][1] +\
				  "\n\t [*] IPv6:\t" + Adaptador[3][1])
		
	elif VIPv4 == True:
		print("\n\t\t [*] IPv4:\t" + IPv4)	# Imprime Si Hay IPv4.
		Log.write("\n\t [*] IPv4:\t" + IPv4)
		
	if VIPv6 == True:
		print("\n\t\t [*] IPv6:\t" + IPv6)	# Imprime Si Hay IPv6.
		Log.write("\n\t [*] IPv6:\t" + IPv6)
		
	print("\n\n\n")
	
	Log.close()
	os.system("Pause > Nul")



#=======================================================================



if __name__ == "__main__":
	
	locale.setlocale(locale.LC_ALL, "es-MX")
	
	while True: 
		
		os.system("cls && Title IpMac.py                "+\
			"By: LawlietJH                "+Version+"    ")
		
		Main()
		

