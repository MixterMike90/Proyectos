#Programa para Calcular el Indice de Masa Corporal de una Persona
#Solicitud de Datos
nombre = str(input("Favor de Introducir su nombre(s): "))
apellido_paterno = str(input ("Favor de Introducir su Primer apellido: "))
apellido_materno = str(input ("Favor de Introducir su Segundo apellido:  "))
edad = int(input("Favor de Introducir su edad: "))
peso = float(input("Favor de Introducir su Peso en Kilogramos: "))
estatura = float(input("Favor de introducir su Estatura en Metros: "))
#Calculo de Indice de Masa Corporal
imc = peso/estatura**2
#Impresión de Datos del Usuario
print("Nombre(s): "+ nombre.title())
print("Apellido Paterno: "+ apellido_paterno.title())
print("Apellido Materno: "+ apellido_materno.title())
print("Edad: " + str(edad) + ' Años')
print("Peso: " +str(peso) + ' Kilogramos')
print("Estatura es: " +str(estatura) + ' Metros')
print("Su indice de Masa Corporal es: ", round(imc,2))
#Mensaje de Observación y Recomendación al Usuario

if imc>=0 and imc<=18.99 :
        print("Su Peso es Bajo, es necesario que visite a un especialista")
elif imc >= 19 and imc <= 24.99:
            print ("Su Masa Corporal esta dentro del Peso normal")
elif imc >=25.00 and imc <= 29.99:
            print("Usted sufre de Sobrepeso, es necesario que visite a un especialista")
elif imc >= 30.00 and imc <= 34.99:
            print("Usted sufre de Obesidad leve, es necesario que visite a un especialista")
elif imc >= 35.00 and imc <= 39.99:
            print("Usted sufre de Obesidad Medía, es necesario que visite a un especialista")
elif imc > 40:
            print("Usted sufre de Obesidad Mórbida, es urgente que visite a un especialista")
else :
    print("FIN")
