# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
####### CAPITULO 49: Expresiones regulares split() y sub() ####################

import re

#Metodo split

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split("es", texto)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto, 4)
print(busqueda)

# Metodo sub()

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto)
print(busqueda)

texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto, 4)
print(busqueda)
