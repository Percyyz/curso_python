#utilizando operadores de comparacion, determina si un numero 
#introducido por el usuario tiene una longitud mayor o igual que 3
#y a su vez es menor que 10

#entrada de datos
numero_usuario:str=input("ingresa un numero :")
longitud:int=len(numero_usuario)
#proceso de datos
comparacion:bool=longitud >=3 and longitud<10
#salida de datos
print(comparacion)


### EJERCICIO 05
#crea un programa que pida al usuario dos numeros y determine si el primero es mayor que el segundo
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultado = (num1 > num2)
print(resultado)