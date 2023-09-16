# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
############ CAPITULO 48: Expresiones regulares findall() ####################

import re

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("e", texto)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("es", texto)
print(busqueda)
