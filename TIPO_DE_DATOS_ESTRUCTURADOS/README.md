# TIPOS DE DATOS ESTRUCTURADOS (TDA - TIPOS DE DATOS ABSTRACTOS)
```python
#lista - sus valores o elementos se pueden actualizar o eliminar
lista=["abel", 20, False, 1.3, .2, ["texto",.2]]

#tupla - sus valores o elementos no pueden ser eliminados o modificados
tupla=("abel", 20, False, 1.3, .2, [])

#diccionarios o objetos - almacenan los datos con clave:valor
diccionarios={"nombre":"antonio","edad":15,"sexo":False}
```
-[!TIP]

-**observacion:** que los tipos de datos estructurados pueden almacenar en su interior otros tipos de datos estructurados.

```python
lista_alumnos=[{
    "nombre":"abel",
    "edad":17,
    "amigos":[]
},{
    "nombre":"percy",
    "edad":20,
    "amigos":[]
}]
```
## METODOS
### 1. convertir texto a lista.
```python
#metodo list
texto="hola"
list(texto) #["h","o","l","a"]

#metodo split - trocea textos en una lista atraves de un limitador
texto="hola como estan alumnitos"
texto.split(" ")

#metodo .join()
texto_largo="este es un texto largo chiquitas y chiquitos"
nuevo_texto=texto_largo.split(" ")
print(nuevo_texto)
print(" ".join(nuevo_texto))
```

### 2. agregar elementos a una lista.
```python
# metodo append - es el metodo que me permite agregar al final de una lista
lista["hola"]
lista.append("mundo")
print(lista) # imprimiraa ["hola","mundo"]

# metodo insrt - es el metodo que me permite agregar elementos en cualquier ubicacion de mi lista
lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0,"flor")
```

### 3. eliminar elementos de una lista.
```python
# metodo (.pop()) - es el metodo que elimina el ultimo elemento de un lista es el contrario de .append().
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop()

# primera opcion - "metodo remove" - este metodo elimina por el nombre del elemento que coincida dentro de mi lista
lista_nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")

# segunda opcion - "metodo pop" - al pasarle por parametro un indice esto lo eliminara de la lista
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop(0)
```

### 4. buscar un elemento en una lista.
```python
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])

pertenecia="edith" in lista_nombres # True False
```
### 5. comparacion de lista.
podrmos hacer uso de los operadores de comparacion para comparar listas

**Ejemplo 1** 
```python
comparar=[1,2,3]>[1,2,4]
print(comparar) #salida: False
```
**Ejemplo 2** 
```python
comparar=[1,2,3]<[1,2,4]
# 1 no por que son iguales en ambas listass
# 2 no por que son iguales en ambas listas
# 3 evalua por que es menor a 4
# entonces la primera lista es menor a la segunda lista
print(comparar) #salida: True
```
### 6. cuidado con las copias.
### 7. fe de erratas(actualizar listas).
```python
lista=[1, 3, 4, 5, 6]
lista[0]=2
print(lista) # [2,3,4,5,6]
```
```python
# modificando lista con diccionario
alumnos=[{
    "nombre":"abel",
    "edad":15
},{
    "nombre":"percy",
    "edad":29
}]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por definir" 
print(alumno) 
```
