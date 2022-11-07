 #    mix=[0,1.0,"dos",3+4j]

#    for i in mix :
    #   print(f"{i:6} - Tipo: {type(i)}")     #imprime el contenido y el tipo de cada valor
#  print(len(mix))           #imprime la cantidad de elementos en la coleccion

# sin_dos = mix[:2] + mix [3:] #se seleccionaron los valores antes y despues de dos 

# print(mix, sin_dos) #se imprimen la lista original y la lista creada tomando los valores antes y despues de dos

# duplicado = mix * 3 #se duplican los valores que se repetiran en la lista
# print (duplicado)     #se imprime los valores de duplicado por la cantidad de veces que se multiplica


cuadrados = [0,1,4,9,16,25]
for i in range (len(cuadrados)) :
    cuadrados[i]  = cuadrados[i] * i
    print (f"{i}**2 = {cuadrados[i]}")
