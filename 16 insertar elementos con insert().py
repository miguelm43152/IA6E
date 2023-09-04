# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
##################### CAPITULO 16: Insertar elementos con insert() ###########################################

# 31 Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert().
#    Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición.
#    Deberás hacer esto utilizando posiciones de lista negativas.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores.insert(6,'magenta')
colores.insert(-1,'turquesa')

print(colores)