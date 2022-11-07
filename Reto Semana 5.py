entrada = input("Hola Introduce tu edad: ")

edad = 0

if entrada.isnumeric():
    edad = int(entrada)
else:
    print("Dato incorrecto, Debes de introducir un numero")
    exit()

if edad<=0 :
    print("Eso no es posible")
elif edad > 115 :
    print("Dato incorrecto, intenta de nuevo")
elif edad < 18 :
    print("Eres menor de edad, no puedes adquirir cigarros")
else : 
    print("Eres mayor de edad, puedes adquirir tus cigarros") 