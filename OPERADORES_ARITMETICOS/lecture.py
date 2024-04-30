### EJERCICIO 01
#realiza un programa que cumpla el siguiente algoritmo 
#utilizando siempre que sea posible operadores en asignacion:
 # 1.- Guarda en una variable numero_magico el valor 12345679 (sin el 8)
 # 2.- lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
 # 3.- Multiplica el numero_usuario por 9 en si mismo
 # 4.- Multilpica el numero_magico por el numero_usuario en si mismo
 # 5.- finalmente muestra el valor final del numero_magico por pantalla

# Paso 1: Guarda el valor del número mágico
numero_magico:int = 12345679

# Paso 2: Lee el número del usuario y asegúrate de que esté entre 1 y 9
numero_usuario:int = int(input("Introduce un número entre 1 y 9: "))

# Paso 3: Multiplica el número del usuario por 9
numero_usuario = numero_usuario*9

# Paso 4: Multiplica el número mágico por el número del usuario
numero_magico = numero_usuario*numero_magico

# Paso 5: Muestra el valor final del número mágico por pantalla
print("El valor final del número mágico es:", numero_magico)

### EJERCICIO 02
#hacer un programa que me saque el promedio de mujeres de un salon 
#donde el total es de 30 alumnos y 20 son varones y el resto mujeres
#entrada de datos
total_alumnos:int=30
cantidad_varones:int=20
cantidad_mujeres:int=total_alumnos-cantidad_varones
promedio_mujeres:float=0

#proceso de datos
promedio_mujeres=(cantidad_mujeres*100)/30

#mostar el dato
print(f"el promedio es de :{promedio_mujeres}%")

### EJERCICIO 03
#crea un programa que calcule el promedio de tres numeros ingresados por el usuario 
nota_uno:int=int("ingrese la primera nota")
nota_dos:int=int("ingrese la segunda nota")
nota_tres:int=int("ingrese la tercera nota")
promedio:int=(nota_uno+nota_dos+nota_tres)/3
print(promedio)

### EJERCICIO 04
#escribe un programa que calcule el area de un circulo pide al usuario que ingrese el radio y muestre 
#el area
radio=float(input("ingrese el radio de un circulo"))
pi:float=3.14
area=pi*radio **2
print(area)




