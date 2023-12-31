# Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Inteligencia Artificial
# Grupo: 6E
####### CAPITULO 46: Modulo datetime con metodo strftime() ####################

import datetime

ahora = datetime.datetime.now()

print(ahora.strftime("Día de la semana abreviado: %a "))
print(ahora.strftime("Día de la semana completo: %A "))
print(ahora.strftime("Mes abreviado: %b "))
print(ahora.strftime("Mes abreviado: %B "))
print(ahora.strftime("Fecha completa: %c "))
print(ahora.strftime("Siglo (empieza a contar desde cero): %C "))
print(ahora.strftime("Día del mes (01 - 31): %d "))
print(ahora.strftime("Día/hora/año: %D "))
print(ahora.strftime("Día del mes (1 - 31): %e "))
print(ahora.strftime("Año en dos dígitos: %g "))
print(ahora.strftime("Año en cuatro dígitos: %G "))
print(ahora.strftime("Mes abreviado: %h "))
print(ahora.strftime("Hora (00 - 23): %H "))
print(ahora.strftime("Hora (01 - 12): %I "))
print(ahora.strftime("Día del año: %j "))
print(ahora.strftime("Mes del 01 al 12: %m "))
print(ahora.strftime("Minuto: %M "))
print(ahora.strftime("Salto de línea: %n"))
print(ahora.strftime("AM o PM: %p "))
print(ahora.strftime("Hora + AM o PM: %r"))
print(ahora.strftime("Hora y minutos: %R"))
print(ahora.strftime("Segundos: %S"))
print(ahora.strftime("Tabulación: %t"))
print(ahora.strftime("Hora, minutos y segundos: %T"))
print(ahora.strftime("Día de la semana (número): %u"))
print(ahora.strftime("Semana del año (empieza en domingo): %U"))
print(ahora.strftime("Semana del año(Condiciones especiales): %V"))
print(ahora.strftime("Semana del año (empieza en lunes): %W"))
print(ahora.strftime("Día de la semana (empieza en domingo): %w"))
print(ahora.strftime("Día/mes/año de dos dígitos: %x"))
print(ahora.strftime("Hora/minutos/segundos: %X"))
print(ahora.strftime("Año corto: %y"))
print(ahora.strftime("Año largo: %Y"))
