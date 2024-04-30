#comparar dos edades ingresadas por el usuario y determinar si son iguales o diferentes

# entrada de datos
edad_uno:str=int(input("ingrese la primera edad :"))
edad_dos:str=int(input("ingrese la segunda edad :"))
#proceso de datos
dyferencia:bool=edad_uno!=edad_dos
comparacion:bool=dyferencia==0
#salida de datos
print(comparacion)


#determinar si un año ingresado por el usuario es anterior al año actual

#entrada de datos
año_ingresado:str=int(input("ingrese el año que desee ."))
año_actual:int=2024
#proceso de datos
comparacion:bool=año_ingresado<año_actual
#salida de datos
print("El año ingresado es anterior al año actual:",comparacion)


#validar si un numero ingresado por el usuario es positivo, negativo o 0

#entrada de datos
numero_ingresado:str=int(input("ingrese un numero :"))
#proceso  de datos
es_positivo:bool = numero_ingresado > 0
es_negativo:bool = numero_ingresado < 0
es_cero:bool = numero_ingresado == 0
#salida de datos
print("El número ingresado es positivo:", es_positivo)
print("El número ingresado es negativo:", es_negativo)
print("El número ingresado es cero:", es_cero)

#determinar si un numero ingresado por el usuario es par y mayor que 10

#entrada de datos
numero_ingresado:str=int(input("ingrese un numero :"))
#proceso de datos
comparacion:bool= numero_ingresado % 2 == 0 and numero_ingresado > 10
#salida de daatos
print("El número ingresado es par y mayor que 10:", comparacion)

#validar si un numero ingresado por el usuario es primo o no

#entrada de datos
numero=4
comparar=numero%2!=0
print("es primo?",comparar)
