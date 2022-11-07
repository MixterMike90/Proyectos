# Longitud de una frase
#========================================================================#
# Crear un programa para identificar la longitud de una palabra ingresada. 
# La palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las siguientes consideraciones:
# Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, 
# se debe imprimir un mensaje que indique que la palabra es correcta
# Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga:
# Hacen falta letras. Solo tiene N letras (siendo N el número de letras de la palabra)
# Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. 
# Tiene N letras ((siendo N el número de letras de la palabra))
#=========================================================================================

frase=input("Introduce una frase: ")
if len(frase)>=4 and len(frase)<9 :
     print("La palabra es correcta")
if len(frase)<4 :
     letras=0
     letras=len(frase)
     print("Hacen falta letras. Solo tiene",letras,"letras")
if len(frase)>8:
     sletras=0
     sletras=len(frase)
     print("Sobran Letras. Tiene",sletras,"letras")


#=======2.-Encuentra el cuadrante====================

# Crear un programa que en base a 2 números de entrada, 
# coordenadas, identifique en cuál de los 4 cuadrantes se encuentra el punto. 
# El programa debe verificar que ninguna coordenada sea 0. Por ejemplo
# Ingrese X: 4
# Ingrese Y: -5
# El punto se encuentra en el cuadrante IV.

print("Introduzca las coordenadas, para saber en que cuadrante se encuentra el punto")
coordenadax=float(input("Introduzca el Valor de X: "))
coordenaday=float(input("Introduzca el Valor de Y: "))

if coordenadax>0 and coordenaday>0 :
    print("El punto se encuentra en el cuadrante I ")
elif coordenadax<0 and coordenaday>0 :
    print("El punto se encuentra en el cuadrante II ")
elif coordenadax<0 and coordenaday<0 :
    print("El punto se encuentra en el cuadrante III ")
elif coordenadax>0 and coordenaday<0 :
    print("El punto se encuentra en el cuadrante IV")
elif coordenadax==0 and coordenaday>0 :
    print("El punto se ubica en el eje de las Abcisas (X),en el lado derecho")
elif coordenadax==0 and coordenaday<0 :
    print("El punto se ubica en el eje de las Abcisas (X),en el lado izquierdo")
elif coordenadax>0 and coordenaday==0 :
    print("El punto se ubica en el eje de ordenadas (Y), en el parte de arriba")
elif coordenadax<0 and coordenaday==0 :
    print("El punto se ubica en el eje de ordenadas (Y), en el parte de abajo")
else :
    coordenadax == 0 and coordenaday == 0
    print("El punto se ubica en el Origen")

print("Fin del Programa".upper())






    




