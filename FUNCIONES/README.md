# FUNCIONES
## Concepto
Matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos` y produce un valor denominado `resultado`.
>[!NOTE]
> Todos los lenguajes de programacion tienen funciones incorporadas (`funciones internas`), y funciones creadas por el usuario (`funciones externas`)

En programacion la funcion es un subprograma, es una estructura que nos permite agrupar codigo, y sus principales objetivos son:
- `NO REPETIR` fragmentos de codigos
- `REUTILIZAR` el codigo en distintos escenarios
## Estructura de una funcion
Una funcion viene `definida` por un `nombre`, sus `parametros` y valor de `retorno` una ves creada la funcion podremos solicitar su ejecucion `invocando` la funcion por su `nombre`.
## Definir el funcion en python
Para definir una funcion en python primero utilizaremos la palabre reservada `def` seguida por el `nombre` de la funcion. A continuacion especificaremos los `parametros` con `()` si es una funcion sin parametros, `(a)` si es asi una funcion con parametros, si se tiviera mas de un parametro iran separados por `,`, finalizaremos la liniea con `:`, en la siguiente linia sin olvidar el identado, comenzara el `cuerpo` de la funcion (micro programa) que puede contener uno o mas sentencias, finalmente devera `retornar` un resultado con la palabra `return`.
>[!TIP]
> Como retorno tambien se puede utilizar la `funcion interna`, `print()`, para depuracion de codigo no es recomendable usuario en produccion. 
> `print()` dentro de una funcion es una herramienta para depurar o comprobar el codigo que una funcion esta haciendo el trabajo de una manera  correcta

 **ejemplo**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return saludo+saludo_dos
    return f"{saludo}, {saludo_dos}"
    # print(f"{saludo},{saludo_dos}")
print(saludo())
# saludo()
```
## Invocar una funcion
Para invocar, (o llamar ejecutar) una funcion solo tendremos que escribir el `nombre` de la funcion seguido por `()` parentesis. 
```python
def saludo():
    print("hola")
# invocando la funcion
saludos()
```
## Retornar un valor
Las funciones pueden retornar (o devolver) un valor.
```python
def uno():
    return 1
uno()
```
>[!WARNING]
>No confundir `print()` con `return`, el valor retornado por `return` nos permite usarlo fuera de su contexto. y `print()` solo mostrara el literal por terminal.
`retunur` devuelve el valor `print` imprime 

**ejemplo**
## retornando multiplos valores
El secreto es hacerlo mediante una tipo de dato estructurado
```python
def varios():
    return 2,3,4
valores()
# retorna tupla co los valores (2,3,4)
```
```python
def lista():
    return ["hola", 45]
lista()
# retorna ["hola", 45]
```
```python
def dicc():
    return {"nombre":"jose", "edad":45}
dicc()
# retorna {"nombre":"jose", "edad":45}
```
## parametros y argumentos.
si una funcion no dispusiera de valores de enttrada estaria limitada en su actuacion. Es por ello que los `parametros` nos permiten variar los datos  que consume una funcion para obtener distintos resultados.

**EJEMPLO**

*crear una funcion que recibe un valor numerico y devuelve su raiz cuadrada*
```python
def sqrt (valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
sqrt(4)
```
cuando llamamos a una funcion con`argumentos` los valores de estos argumentos se copian en los correspondientes `parametros` dentro de la funcion.
```python
def ejem(a,b,c):
    return(a+b+c)
ejem(4,5,6)
```
### argumentos nominales.
en esta aproximacion los argumentos no son copiados en un orden especifico sino que **se asignan por nombre a cada parametro**, ello nos permite evitar el problema de conocer o recordar cual es el orden de los parametros en la definicion de la funcion. 

Para utilizarlo, basta con realizar una asignacion de cada argumento es la propia llamada de funcion.

**EJEMPLO**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una
        frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos nominales
build_cpu(num_core=4, familia="intel", frecuencia=2.7)
```
### argumentos posicionales.
Los argumentos son copiados en un orden especifico, en este caso debemos conocer o recordar cuale es el orden de los parametros 

**EJEMPLO**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una
        frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos posicionales
build_cpu("intel", 4, 2.7)
```
## parametros por defecto
Es posible espesificar **valor por defecto** en los parametros en una funcion,
en el caso de que no se promocione un valor al argumento en la llamada a la funcion, el parametro correspondiente tomara el valor definido por defecto.

**EJEMPLO**
```python
def alumnos(nombre, apellido,estado="aprobado"):

alumnos("percy","yarihuaman")
alumnos("percy","yarihuaman","desaprobado")
```
## Empaquetado/Desempaquetado de argumentos posicionales (tarea)
El **empaquetado y desempaquetado de argumentos posicionales** en Python se refiere a la capacidad de pasar un número variable de **argumentos** a una función utilizando el operador `*` **para empaquetar (en la llamada a la función)** y **desempaquetar (dentro de la definición de la función)**. Esto permite manejar listas de argumentos de longitud variable de manera flexible y conveniente.
### Empaquetar argumentos posicionales.
En Python, el **empaquetado de argumentos posicionales** se refiere a la capacidad de una función para recibir un **número variable de argumentos**.

Al usar el operador `*` delante del **nombre** de un **parámetro posicional** en una función, estamos indicando que todos los argumentos adicionales pasados a la función se **agruparán en una tupla**.

>EJEMPLO 1
```python
def ejemplo_empaquetado(*args):
    print("Los argumentos empaquetados en una tupla son:", args)
# Llamamos a la función con varios argumentos
ejemplo_empaquetado(1, 2, 3, 'a', 'b', 'c')
```
>EJEMPLO 2
```python
def mi_funcion(*args):
    for arg in args:
        print(arg)
mi_funcion(1, 2, 3, 4)
```
En este ejemplo 2, la función `mi_funcion` puede aceptar cualquier número de argumentos posicionales, los cuales se almacenan en la tupla `args`. Al llamar a `mi_funcion(1, 2, 3, 4)`, los valores `1`, `2`, `3` y `4` se empaquetan en `args` y se imprimen uno por uno dentro del bucle `for`.
### Desempaquetar argumentos posicionales
Además del empaquetado de argumentos posicionales, también existe el **desempaquetado de argumentos posicionales** cuando se llama a una función. Esto se logra utilizando el operador `*` al pasar los **argumentos**.
> EJEMPLO 
```python
def sumar(a, b, c):
    return a + b + c

numeros = (1, 2, 3)
resultado = sumar(*numeros)
print(resultado)  # Imprime 6
```
## Empaquetado/Desempaquetado de argumentos nominales
El **empaquetado y desempaquetado de argumentos nominales** en Python se refiere a la capacidad de pasar un número variable de **argumentos con nombre** a una función utilizando el operador `**` **para empaquetar (en la llamada a la función)** y **desempaquetar (dentro de la definición de la función)**. Esto **permite manejar diccionarios de argumentos** de longitud variable de manera flexible y conveniente.
### Empaquetado de argumentos nominales
Cuando usamos el operador `**` delante del **nombre de un parámetro** con nombre en una función, estamos señalando que los **argumentos** pasados a la función como pares **clave-valor se agruparán en un diccionario**.
> EJEMPLO 
```python
def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(f'{clave}: {valor}')

# Llamada a la función con argumentos nominales empaquetados
imprimir_datos(nombre='Ana', edad=28, ciudad='Barcelona')
```
### Desempaquetado de argumentos nominales
El **empaquetado de argumentos nominales** en Python se realiza utilizando el operador `**` **seguido de un diccionario** al llamar a una función. Este operador permite pasar un número variable de argumentos con nombre **(clave-valor)** a una función de manera que puedan ser manejados como un diccionario dentro de la función.
> EJEMPLO 
```python
def saludar(nombre, edad):
    print(f'Hola {nombre}, tienes {edad} años.')

# Diccionario con los datos que queremos pasar como argumentos nominales
datos = {'nombre': 'Pedro', 'edad': 32}

# Desempaquetamos los argumentos nominales para llamar a la función
saludar(**datos)
```