# 1.  crear una funcion que reciba por argumento n nueros y retorne una lista con los numeros pares
def numeros(*numeros):
   lista_pares=[]
   for i in numeros:
      if i %2==0:
         lista_pares.append(i)
   return lista_pares
print(numeros(1,2,3,4,5,6,7,8,9,10))
# tambien podemos hacer hasi por comprension
#  return num for num in numeros if num %2==0
# print(numeros(1,2,3,4,5,6,7,8,9,10))


# 2. cerar tres funciones para los siguientes casos 
## calcular el numero menor
## calcular el numero mayor
## calcular la suma de todos los numeros
## se le pasara por argumento n numeros
def calcular_menor(*numeros):
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor

def calcular_mayor(*numeros):
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor

def calcular_suma(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma
numeros = [3, 5, 7, 2, 8]
menor = calcular_menor(*numeros)
mayor = calcular_mayor(*numeros)
suma = calcular_suma(*numeros)
print(f"El número menor es: {menor}")
print(f"El número mayor es: {mayor}")
print(f"La suma de los números es: {suma}")

## TAREA 
# CREAR UNA LISTA DE ALUMNOS CON LOS SIGUIENTES CAMPOS
# NOMBRE, APELLIDO, EDAD, CELULAR Y EMAIL.
# ACTUALIZAR LOS REGISTROS CON UN CAMPO MAS TODOS TENDRAN EL CAMPO EL PROGRAMA DE ESTUDIOS DE ENFERMERIA 
# BUSCAR EL SEGUNDO REGISTRO Y ACTUALIZAR SU EDAD A 50 AÑOS

lista_alumnos=[
    {
        "nombre":"percy",
        "apellido":"yarihuman",
        "edad":20,
        "celular":927870885,
        "email":"percynoeyarihuaman@gmail.com"
    },
    {
        "nombre":"jose",
        "apellido":"garriazo",
        "edad":25,
        "celular":934762111,
        "email":"josegarriazo@gmail.com"
    },
    {
        "nombre":"carlos",
        "apellido":"castillo",
        "edad":21,
        "celular":940788001,
        "email":"castillo@gmail.com"
    },
    {
        "nombre":"miguel",
        "apellido":"solis",
        "edad":30,
        "celular":922009343,
        "email":"solismiguel@gmail.com"
    },
]
def agregar_programa_estudios(e):
    e["programa_estudios"] = "Enfermería"
    return e
nueva_lista = list(map(agregar_programa_estudios, lista_alumnos))
nueva_lista1=lista_alumnos[1]["edad"]=50
print(nueva_lista)