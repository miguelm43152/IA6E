# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
########### CAPITULO 23: El condicional IF ELIF ELSE E INPUT #########################

# 40.- Al siguiente código añádele un par de rangos de edad.
# Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
        print("eres mayor de edad")
elif edad >= 18 and edad <= 100:
	print('Ya estas viejo.')
elif edad >= 100 and edad <= 120:
        print( "Ya estas muerto" )
else:
	print('Edad no válida.')
