# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
############# CAPITULO 20: Cómo convertir tuplas a listas y viceversa ################################

# 35.- Convierte la siguiente lista en una tupla y asegúrate que se haya
#convertido en tupla correctamente imprimiendo en la consola el tipo de elemento que es.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

print( "Esto es una lista:",colores )

colores = tuple(colores)

print( "Ahora la convertimos a una tupla:",colores)

print( "y sino la creen, mostramos el tipo de dato:",type(colores))
