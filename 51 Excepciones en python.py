# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
####### CAPITULO 51: Manejo de excepciones en Python ####################

reinicio = True

while reinicio:
    try:
        num1 = int( input( "Introcuce un número para multiplicar: " ) )
        num2 = int( input( "Introcuce otro número para multiplicar: " ) )
    except ValueError:
        print( "No has introducido un número. Vuelve a intentarlo.")
    else:
        print( "El resultado es:", num1 * num2)
    finally:
        pregunta = input( "¿Quieres seguir multiplicando? Introduce S/N:\n")
    if pregunta == "N" or pregunta == 'n':
        reinicio = False
    else:
        print( "De acuerdo, vamos a seguir multiplicando.")
