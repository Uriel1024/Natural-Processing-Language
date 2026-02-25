#Construir un modelo que detecte fechas numericas en el formato dd-mm-aaaa, esto con fechas validas
import re
#si tiene 31 dias es impar, 30 dias es par, si es divisible entre 4 febrero tiene 28 dias
#caracter, inicio, enmedio y final  


prueba = "41-11-2023"
#prueba = input("Ingresa una fecha: ")
#El primer bloque sirve para mostrar los dias del 01 al 09 0[1-9], el or es para los dias del 10 al 29 [12]01-9]  y el tercero es para el 30
#El segundo valida si es un mes par hasta el 12
#El tercer bloque es solo valida que tenga 4 digitos y que se encuentre al final
#Despues se hace practicamente lo mismo con el bloque pero para meses que tienen 31 dias que son los impares

#patron = r"^((0[1-9]|[12][0-9]|3[0])-(4|6|8|10|12|04|08)-\d{4}$)|((0[1-9]|[12][0-9]|3[1])-(1|3|5|7|9|11|01|03|05|07|09)-\d{4}$)|((0[1-9]|1\d|2[0-8])-(2|02)-\d{4}$)"
patron = r"^((0[1-9]|[12][0-9]|3[0])-(0?(4|6|9)|11)-\d{4}$)|((0[1-9]|[12][0-9]|3[1])-(0?(1|3|5|8|7)|10|11)-\d{4}$)|((0[1-9]|1\d|2[0-8])-(2|02)-\d{4}$)"


#para reducir espacio en el codigo podemos hacer lo siguiente 0?(||||)||
if re.search(patron,prueba):
    print(f"La fecha {prueba} es valida")
else:
    print(f"La fecha {prueba} no es valida")




