
#primer ejemplo de if estructurado
# edad:int=int(input("escriba su edad :"))
# if edad>=18:
#      print("eres mayor")
# else:
#      print("eres menor")

# #segundo ejemplo if almacenado en variable
edad:int=int(input("escriba su edad :"))
respuesta:str="eres mayor" if edad>=18 else "eres mayor"
print (respuesta)

# # crear un programa que me imprima las 5 vocales
vocales:str="aeiou"
for n in range(0,5):
     print(vocales[n])

# # crear un progrma que me muestre los 8 primeros numeros pares
contador=0
for i in range(1,17):
    if i%2==0:
        contador+=1
        print(f"{i} es par numero {contador}")

# # crear un programa que me pida al usuario escribir una oracion y mostrar por la terminal la cantidad de vocales 
# # a tiene esa oracion
# # OJO SOLO LAS a MINUSCULA
oracion:str=input("escribe una oracion :")
contador_a=0
for n in range(0,len(oracion)) :
    if oracion[n]=="a":
        contador_a=contador_a+1
print(f"la cantidad de lestras a que tengo es {contador_a}")

# crear un programa que me cuente la cantidad de comas y me muestre sus indices
cadena:str = input("Ingrese una cadena de texto: ")
contador:int=0
for indice,letra in enumerate(cadena):
    if letra ==",":
        print(f"su indice es {indice}")
        contador+=1
print(f"la cantidad de comas es {contador}")

# escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido
# (desde 1 hasta su edad)
edad:int=int(input("ingrese su edad :"))
for i in range(1,(edad)):
    print(f"su edad cumplido: {i} años")
print (f"todos los años que ha cumplido es: {edad} años")

# crear un programa que me pida el nombre de tres personas i guarde en una variable global la ultima 
# letra de sus nombres.
# mostrar por pantalla la variable global con las ultimas letras de del nombre 
# de cada persona.

ultima_letra:str=""
for _ in range(3):
    nombre:str=input("escribe tu nombre")
    last_leter:str=nombre[-1]
    ultima_letra+=last_leter
print(ultima_letra)

# crear un programa que muestre por terminal las siguiente figura
#a
#ee
#iii
#oooo
#uuuuu
letras:str= "aeiou"
for i in range(len(letras)):  
    print(letras[i] * (i + 1))