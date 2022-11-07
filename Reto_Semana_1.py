#Reto de la semana 1 de Octubre 2022

#Puntos a Cumplir

# 1-Se solicitara al usuario el año actual y un año cualquiera
# 2-Que se despliegue en pantalla cunatos años han pasado desde el año ingresado
# al año actual o cuantos años faltan para llegar a ese año
# 3-Se debe de tener en cuenta que si falta o ha pasado un año, se debera de mostrar 
# el mensaje adecuado
# 4-Se deberá notificar si se ha ingresado el mismo año


actual = input("Introduce el año actual: ")
año_actual=int(actual)
cualquiera=input("Introduce otro año para calcular: ")
año_cualquiera=int(cualquiera)
diferencia=int

if  año_actual==año_cualquiera :
    print("Has introducido el mismo año que el actual")
elif año_actual!=año_cualquiera and año_actual>año_cualquiera :
        diferencia=año_actual - año_cualquiera
        if diferencia>10 :
            print("Han pasado ",diferencia,"años desde el año que has introducido") 
        elif diferencia<2 :
            print("Desde el año",año_actual,"ha pasado",diferencia,"año") 

elif año_actual!=año_cualquiera and año_cualquiera>año_actual :
    diferencia=año_cualquiera-año_actual
    if diferencia==1 :
        print("Para llegar a",año_cualquiera,"hace falta",diferencia,"año")
    elif diferencia>1 :
        print("Faltan",diferencia,"años para llegar al año que has introducido")


