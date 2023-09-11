# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo 6E
############# CAPITULO 28: bucle while con condicional if ######################

x = 0
while x <= 30:
    if x == 4 or x == 6 or x == 10:
        print( "Se saltó el valor", x, 'de x.')
        x += 1
        continue
    if x == 15:
        print("Se rompió la ejecución del bucle cuando x valía " + str(x) +".")
        break
    print( x)
    x += 1