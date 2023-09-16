# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
####### CAPITULO 43: Variables globales, locales y funciones ####################

def funcion1():
	global num1
	num1 = 10

funcion1()

print(num1)

def funcion1():
	pass
def funcion2():
	print('String en la función anidada.')

funcion1()
