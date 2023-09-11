# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
############# CAPITULO 29: El bucle for ######################

# 46 Crea un bucle for que itere la siguiente tupla y muestre una 
#    frase como esta en cada iteración: 'El color es: ' + color + '.'.

####### solución del blog.

colores = ('rojo', 'azul', 'verde', 'amarillo')

for x in colores:
	print('El color es: ' + x + '.')


############### solución propuesta

colores = ('rojo','azul','verde','amarillo')
mensaje = "El color es: "

for x in range(len(colores)):
	
    if x == (len(colores) - 1):
         mensaje = mensaje + colores[x] + ". "
         continue
    if x == (len(colores) - 2):
         mensaje = mensaje + colores[x] + " y "
         continue
    mensaje = mensaje + colores[x] + ", "

print(mensaje)