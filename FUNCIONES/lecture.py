# return devuelve valores que podre hacer uso
# crear una funcion que retorne el numero 10, y muestre por terminal si es par
# siempre que el valor que retorne mi funcion se utilice en mas sentencias u operaciones hacer uso de return
def diez():
    return 10
if diez %2==0:
    print("es par")
else:
    print("es impar")
# print solo muestra por terminal

## return cuando queremos que muestre una funcion devuelva o retorne un tipo de dato o un tipo de dato estructurado

# crear una funcion que me muestre el producto de dos numeros
def producto(a,b):
    return a*b

# crear una funcion que em retorne una lista de tres numeros
def lista_nemeros():
    return[1,2,3]


# print usaremos cada vez que nuestra funcion retorne un mensaje
# crear uan funcion que por parametro reciba un nombre y retorne un mensaje de bienvenida con el nombre
def mensaje(nombre):# el de parentesis es parametro
    print(f"hola,{nombre},vienvenido")
mensaje("juan")# en caso de aqui se llama argumento

# crear una funcion que reciba por prametros una lista de numeros y que me dubuelva el numero menor, mostrar por terminal el 
# valor retornado por la funcion
lista=[2,3,4,5,18,1,9]
def Min(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
print(Min(lista))

# # crear una funcion que reciba como parametro un nombre y edad de una persona mi funcion debera retornar un diccionario con los datos y luego mostrar por terminal 
# # el valor de retorno de mi funcion
nombre="juan"
edad=20
def diccionario(nombre,edad):
    return {"nombre": nombre, "edad": edad}
datos_persona = diccionario(nombre, edad)
print(f"Datos de la persona: {datos_persona}")

# # EJERCICIO CON ARGUMENTO EMPAQUETADO/DESEMPAQUETADO POSICIONALES
def suma(*valores):
    nueva_lista=list(valores)
    nueva_lista[0]=10
    print(nueva_lista)
suma(2,4,6,3,4)

# # EJERCICIO CON ARGUMENTO EMPAQUETADO/DESEMPAQUETADO NOMINALES
def alumnos(**list_nombres):
    print(list_nombres)
alumnos(nombre="percy", apellido="yarihuman", edad=21)
# tambien podemos modificar nuestro diccionario
list_nombres={
    "nombre":"hola"
}
list_nombres["nombre"]="percy"

## EJEMPLOS DE LAMBDA

saludo=lambda: "hola"
print(saludo())

saludo = lambda n,a:f"hola, {n},{a}"
print(saludo("ruth","castillo"))

# crear un programa anonimo que reciba por parametro una de lista de 5 numeros y retorne dos listas una con numeros pares 
# y otra con numeros impares
lista=[2,6,4,8,2,12,45,67,87,]
pares=lambda l:[n for n in lista if n%2==0]
impares=lambda l:[n for n in lista if n%2!=0]
print(pares(lista))
print(impares(lista))

## reducir en pocas linias de codigo
lista = [2, 6, 4, 8, 2, 12, 45, 67, 87]
pares_impares = lambda l: ([n for n in l if n % 2 == 0], [n for n in l if n % 2 != 0])
print(pares_impares(lista))

## funciones callback
int(input)
def mensaje(m):
    print (m)

def pedir_nombre():
    nombre=input("ingresa tu nombre")
    return nombre
mensaje(pedir_nombre())

## map(): sirve para iterar una lista
lista=[4,5,6,7,8,9]
nueva_lista=list(map(lambda x:x+1, lista)) # por defecto retorna una lista
print(nueva_lista)

# tengo una lista de alumnos que todos ellos aprobaron y pasa al tercer semestre
# en mi lista todos estan en el segundo semestre por lo que tendremos que crear una solucion que cambie el campo de semestre de 2 a 3
lista_alumnos=[
    {
        "nombre":"percy",
        "edad":20,
        "semestre":2
    },
    {
        "nombre":"bretmer",
        "edad":18,
        "semestre":2
    },
    {
        "nombre":"erick",
        "edad":19,
        "semestre":2
    },
]
def objeto (e):
    if "semestre" in e:
        e["semestre"]=e["semestre"]+1
    e["carrera"] = "apsti"
    return[
        e
    ]

nueva_lista=list(map(objeto, lista_alumnos))
print(nueva_lista)

## filter():
# devolver los numeros Pares de una lista
lista=[3,8,3,6,2,10,12,18,20]
nueva_lista=list(filter(lambda x:x%2==0,lista))
print(nueva_lista)

lista_alumnos=[
    {
        "nombre":"percy",
        "edad":20,
        "semestre":2
    },
    {
        "nombre":"bretmer",
        "edad":18,
        "semestre":2
    },
    {
        "nombre":"erick",
        "edad":19,
        "semestre":2
    },
]
nueva_lista=list(filter(lambda x:x["edad"]<20, lista_alumnos))
print(nueva_lista)