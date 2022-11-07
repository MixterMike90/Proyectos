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

# Se le pide al usuario introduzca la frase que guste en el programa
frase=input("Introduce una frase: ")
#Se va a evaluar el contenido de las letras que conforma la frase introducida por el usuario
#Primero se evaluara si cumple con la primera condicion solicitada 
if len(frase)>=4 and len(frase)<9 :
     print("La palabra es correcta")
#En caso que no cumpla la primera condicion se pasara a la siguiente para saber si cumple con la 
#Segunda condicion, dando salida a pantalla como lo solicita los puntos requeridos
if len(frase)<4 :
     letras=0
     letras=len(frase)
     print("Hacen falta letras. Solo tiene",letras,"letras")
#En caso de que no cumpla con las otras condiciones se determinara que cumpla con la tercera 
#condicion,dando salida a pantalla como lo solicita los puntos requeridos
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

#Primero Se solicitan los datos , en este caso el valor de X y el de Y
print("Introduzca las coordenadas, para saber en que cuadrante se encuentra el punto")
coordenadax=float(input("Introduzca el Valor de X: "))
coordenaday=float(input("Introduzca el Valor de Y: "))

#Se realizaron los criterios de evaluacion para que el valor dado por el usuario del punto a ubicar
#Nos indique el programa que cuadrante se ubica el punto 
#O en que eje se ubica o si todavia esta en el origen, mostrando en que cuadrante esta por medio de 
#Un mensaje
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






    




