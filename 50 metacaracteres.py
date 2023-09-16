# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
####### CAPITULO 50: Secuencias especiales ####################
####### Metacaracteres en python           ####################

import re

texto = "Bienvenidos a Programación fácil y bienvenidos al curso de Python."
buscar = re.findall("[c-g]", texto)
print(buscar)

texto = "¿Van al zoológico?"
buscar = re.findall("zo{2}lógico", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")

texto = "El futuro es ahora."
buscar = re.findall("pasado|futuro", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")

texto = "La programación es fácil."
buscar = re.findall("progra..ción", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")


import re
texto = "Se acerca el invierno."
buscar = re.findall("^Se acerca", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")

import re

texto = "Se acerca el invierno."
buscar = re.findall("vierno.$", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")
