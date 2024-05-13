
#primer ejemplo de if estructurado
edad:int=int(input("escriba su edad :"))
if edad>=18:
     print("eres mayor")
else:
     print("eres menor")

#segundo ejemplo if almacenado en variable
edad:int=int(input("escriba su edad :"))
respuesta:str="eres mayor" if edad>=18 else "eres mayor"
print (respuesta)

# crear un programa que me imprima las 5 vocales
vocales:str="aeiou"
for n in range(0,5):
     print(vocales[n])

# crear un progrma que me muestre los 8 primeros numeros pares
contador=0
for i in range(1,17):
    if i%2==0:
        contador+=1
        print(f"{i} es par numero {contador}")

# crear un programa que me pida al usuario escribir una oracion y mostrar por la terminal la cantidad de vocales 
# a tiene esa oracion
# OJO SOLO LAS a MINUSCULA
oracion:str=input("escribe una oracion :")
contador_a=0
for n in range(0,len(oracion)) :
    if oracion[n]=="a":
        contador_a=contador_a+1
print(f"la cantidad de lestras a que tengo es {contador_a}")

# crear un programa que me cuente la cantidad de comas y me muestre sus indices
usuario:str=input("ingrese una oracion :")
contador=0
for n in range(0,len(usuario)):
    if usuario[n]==",":
       contador+=1
    print(f" la cantidad de comas es {n}")
print(contador)


