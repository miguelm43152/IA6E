# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
########## CAPITULO 43: Importar módulos y funciones lambda ##################

import math

def area(radio):
	resultado = round(math.pi * radio * radio,2)
	print(resultado)

area(2)

area = lambda radio: print(round(math.pi * radio * radio,2))

area(2)
