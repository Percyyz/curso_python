# 2.-ALGORITMO QUE CALCULE EL PROMEDIO DE TRES NUMEROS
#entrada de datos
notaUno:int=14
notaDos:int=12
NotaTres:int=17
#proceso de datos
promedio:int=(notaUno+notaDos+NotaTres)/3
#salida de datos
print(promedio)

# 4.-ALGORITMO QUE CALCULE EL VOLUMEN DE UNA ESFERA
radio = float(input("Ingrese el radio de la esfera: "))
#  Calcular el área de la esfera
pi = 3.14  # Valor aproximado de pi
area = 4 * pi * radio ** 2
#Mostrar el resultado
print("El área de la esfera es:", area)

# 5.-ALGORITMO QUE CALCULE EL AREA DE UN TRIANGULO
#entrada de datos
base = float(input("Ingresa la longitud de la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
#proceso de datos
area = (base * altura) / 2
#salida de datos
print("El área del triángulo es:", area)

# 6.-ALGORITMO QUE DETERMINE UN VIAJE DE IDA Y VUELTA AL SOL A UNA VELOCIDAD CONSTANTE IGUAL AL DE LA LUZ
#entrada de datos
distancia = 149.6e6  # distancia en kilómetros
velocidad = 299792  # velocidad en kilómetros por segundo
#proceso
tiempo_ida = distancia / velocidad
tiempo_vuelta = tiempo_ida * 2
#salida
print("Tiempo de ida al Sol:", tiempo_ida, "segundos")
print("Tiempo de ida y vuelta al Sol:", tiempo_vuelta, "segundos")

# 9.-ALGORITMO QUE CALCULE EL AREA DE UN CUADRADO
#entada de datos
lado = float(input("Ingresa la longitud de un lado del cuadrado: "))
#proceso de datos
area = lado **2
#salida de datos
print("El área del cuadrado es:", area)

# 10.-ALGORITMO QUE CONVIERTA KILOMETROS A MILLAS
#entrada de datos
distancia_km = float(input("Ingrese la distancia en kilómetros: "))
#proceso de datos
constante_conversion = 0.621371
distancia_millas = distancia_km * constante_conversion
#salida de datos
print("La distancia en millas es:", distancia_millas)

