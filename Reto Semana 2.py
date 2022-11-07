i = 0
def comprobacioncontraseña(contraseña):
    numer=False
    for i in range(len(contraseña)):
        if contraseña[i].isnumeric():
            numer = True
        if numer:
         return True
        else:
          return False
          
contraseña=input("Ingrese una contraseña: ")
verificarcontraseña = comprobacioncontraseña(contraseña)
if verificarcontraseña is True:
    input("Ingrese la contraseña nuevamente: ")
    print("Contraseña correcta")
    print("Fin del Programa")

elif verificarcontraseña is False:
    while i<3 :
        print("La contraseña debe de iniciar con un numero")
        input("Ingrese una contraseña: ")
        input("ingrese la contraseña nuevamente: ") 
        print("Las contraseñas no coinciden")    
        i+=1
    print("Fin del Programa")


        


