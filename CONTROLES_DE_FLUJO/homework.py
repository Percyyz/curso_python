# 1.-DISEÑAR UN ALGORITMO QUE DETERMINE SI EL PRIMERO DE DOS NUMEROS ES EL MAYOR
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
if numero1>numero2:
   print("el primer numero es mayor")
else:
   print("el segundo numero es mayor")

# 3.-ALGORITMO QUE VALIDE SI UN NUMERO SE ENCUENTRA EN EL RANGO 1 A 100
#entrada de datos
número:int=int(input("ingrese un numero :"))
#proceso 
if número >= 1 and número <= 100:
    print("El número está en el rango de 1 a 100.")
else:
    print("El número está fuera del rango de 1 a 100.")

# 8.-ALGORITMO QUE COMPARE SI DOS NUMEROS SON IGUALES DIFERENTES O SI UNO ES EL DOBLE DEL OTRO
#entrada de datos
numero_uno:int=int(input('ingresa un numero entero positivo: '))
numero_dos:int=int(input('ingresa segundo numero entero positivo:'))
#comparacon de datos
if numero_uno == numero_dos:
  print(f'el numero {numero_uno} es igual al numero {numero_dos}')
elif numero_uno != numero_dos:
  if numero_uno*2 == numero_dos:
    print(f'el numero {numero_dos} es el doble del {numero_uno}')
  else:
    print(f'el numero {numero_uno} es distinto al numero {numero_dos}')

# 15.-ESCRIBIR UN PROGRAMA PARA UNA EMPRESA QUE TIENE SALAS DE JUEGOS PARA TODAS LAS EDADES Y QUIERE CALCULAR DE FORMA 
##### AUTOMATICA EL PRECIO QUE DEBE COBRAR A SUS CLIENTES POR ENTRAR. EL PROGRAMA DEBE PREGUNTAR AL USUARIO LA EDAD DEL CLIENTE
##### Y MOSTRAR EL PRECIO DE LA ENTRADA. SI EL CLIENTE ES MENOR DE 4 AÑOS PUEDE ENNTRAR GRATIS, SI TIENE ENTRE 4 Y 18 AÑOS 
##### DEBE PAGAR s/.5 Y SI ES MAYOR DE 18 AÑOS, s/18
edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 18
print("El precio de entrada es: s/.", precio_entrada)

