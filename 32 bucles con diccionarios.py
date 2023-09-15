# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
############ CAPITULO 32: Bucles con diccionarios ####################
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

# 49.- Itera el diccionario teclado1 con un solo
# bucle for que muestre esto en la consola:

print( "\nInformación teclado1:")
for i in teclado1:
    print("\t" + i + ': ' + teclado1[i] )

print( "\nInformación teclado2:")
for i in teclado2:
    print("\t" + i + ': ' + teclado2[i] )

print( "\nFin del programa...\n")
