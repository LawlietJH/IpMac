import psutil
import os

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
