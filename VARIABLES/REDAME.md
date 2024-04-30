# VARIABLES
VARIABLE es un lugar donde se almacenan un dato
-Una variable es un contenedor que almacena un valor o conjunto de valores en la memoria de un ordenador y les asigna un nombre único.

```python
numero_magico=6324781711
print(id(numero_magico))
```
realiza un programa que cumpla el siguiente algoritmo 
utilizando siempre que sea posible operadores en asignacion:

 1.- Guarda en una variable numero_magico el valor 12345679 (sin el 8).

 2.- lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
 
 3.- Multiplica el numero_usuario por 9 en si mismo
 
 4.- Multilpica el numero_magico por el numero_usuario en si mismo
 
 5.- finalmente muestra el valor final del numero_magico por pantalla

```python
#Paso 1: Guarda el valor del número mágico
numero_magico:int = 12345679
#Paso 2: Lee el número del usuario y asegúrate de que esté entre 1 y 9
numero_usuario:int = int(input("Introduce un número entre 1 y 9: "))
#Paso 3: Multiplica el número del usuario por 9
numero_usuario = numero_usuario*9
#Paso 4: Multiplica el número mágico por el número del usuario
numero_magico = numero_usuario*numero_magico
#Paso 5: Muestra el valor final del número mágico por pantalla
print("El valor final del número mágico es:", numero_magico)
```