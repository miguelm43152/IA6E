# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
######## CAPITULO 33: Metodos con diccionarios en python################

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

# 50.- Elimina el diccionario teclado1 entero .
# De teclado2 elimina las claves 'Categoría' y 'Precio'.
# Muestra la última clave ('Modelo') que queda en la consola.

del teclado1 # Esta línea elimina la variable 'teclado1' por completo

print( 'El diccionario "teclado2" tiene',len( teclado2),'elementos:\n',teclado2,'\n')

# Nótese que se usa la función len() para contar los elementos que tiene
# un diccionario. En este caso, estamos contando los elementos que tiene
# el diccionario "teclado2"

del teclado2['Categoría']
del teclado2['Precio']

print( 'El diccionario "teclado2" ahora tiene',len( teclado2),'elemento:\n',teclado2)
