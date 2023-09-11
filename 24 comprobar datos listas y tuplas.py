# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
##################### CAPITULO 24: Comprobar datos en listas y tuplas ###########################################

colores = ("rojo", "amarillo", "azul", "verde")

entrada = input("Ingrese un color:\n\t")
entrada = entrada.lower()
if entrada in colores[0]:
    print( entrada, "se encuentra en la lista.")    
elif entrada in colores[1]:
    print( entrada, "se encuentra en la lista.")    
elif entrada in colores[2]:
    print( entrada, "se encuentra en la lista.")    
elif entrada in colores[3]:
    print( entrada, "se encuentra en la lista.")    
else:
    print( entrada, "no se encuentra en la lista." )

#print( entrada, "es el color ingresado.")