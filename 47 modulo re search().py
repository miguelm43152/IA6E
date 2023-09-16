# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
############ CAPITULO 47: Expresiones regulares search() ####################

import re

texto = "Bienvenidos a Programación fácil"
busqueda = re.search("i", texto)
print(busqueda)

busqueda = re.search("Bienvenidos", texto)
print(busqueda)
