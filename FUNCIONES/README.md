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
## Funciones internas de python (Tarea)
Python cuenta con muchas funciones internas (built-in functions) que están disponibles para su uso directo sin necesidad de importar ningún módulo adicional.
### 1. funciones de conversion de tipos de datos
En Python, las funciones de conversión de datos permiten `transformar` un tipo de dato en otro. Esto es útil cuando necesitas operar con diferentes tipos de datos o cuando deseas asegurarte de que un `valor` tenga el tipo correcto para cierta operación.
#### Funcion int:
En python, la funcion `int` comvierte el valor a un entero.
>EJEMPLO
```python
num_str = "123"
num_int = int(num_str)  # Convierte la cadena "123" a un entero
print(num_int)  # Salida: 123
```
#### Funcion float:
En python, la funcion `float` convierte un valor a un número de punto flotante (decimal).
>EJEMPLO
```python
num_str = "123.45"
num_float = float(num_str)  # Convierte la cadena "123.45" a un flotante
print(num_float)  # Salida: 123.45
```
#### funcion str:
En python, la funcion `str` convierte un valor a una cadena de caracteres.
>EJEMPLO
```python
num_int = 123
num_str = str(num_int)  # Convierte el entero 123 a cadena "123"
print(num_str)  # Salida: "123"
```
#### Funcion bool:
En python, la funcion `bool` convierte un valor a un booleano. Los valores que se consideran False en Python (como 0, None, listas, conjuntos o diccionarios vacíos) se convertirán a False; todos los demás valores se convertirán a True.
>EJEMPLO
```python
value = 0
bool_value = bool(value)  # Convierte 0 a False
print(bool_value)  # Salida: False
```
>EJEMPLO
```python
value = 
bool_value = bool(value)  # Convierte 1 a True
print(bool_value)  # Salida: True
```
### 2. Funciones de iteracion y generacion
En Python, las funciones de iteración y generación son fundamentales para trabajar con colecciones de datos de manera eficiente.

son funciones integradas que se utilizan para generar y manipular secuencias de datos de manera eficiente.
#### Funcion range():
En python `range()` es una función que genera una secuencia de números.
>EJEMPLO
```python
# Generar una secuencia de 0 a 4
for i in range(5):
    print(i)  # Salida: 0 1 2 3 4
```
```python
# Generar una secuencia de 1 a 9
for i in range(1, 10):
    print(i)  # Salida: 1 2 3 4 5 6 7 8 9
```
```python
# Generar una secuencia de 0 a 10 con un paso de 2
for i in range(0, 11, 2):
    print(i)  # Salida: 0 2 4 6 8 10
```
#### Funcion enumerate():
En Python, `enumerate()` es una función incorporada que agrega un contador a un iterable y lo devuelve en forma de un objeto enumerado.
>EJEMPLO
```python
# Enumerar una lista
mi_lista = ['a', 'b', 'c']
for indice, elemento in enumerate(mi_lista):
    print(indice, elemento)  # Salida: 0 a, 1 b, 2 c

```
```python
# Enumerar una cadena con un índice inicial diferente
mi_cadena = "hola"
for indice, letra in enumerate(mi_cadena, start=1):
    print(indice, letra)  # Salida: 1 h, 2 o, 3 l, 4 a
```
#### Funcion zip():
En Python, la función `zip()` se utiliza para combinar dos o más iterables (como listas, tuplas, etc.) en un solo iterable de tuplas, donde cada tupla contiene elementos que ocupan la misma posición en los iterables originales.
>EJEMPLO
```python
# Combinar dos listas
nombres = ['Alice', 'Bob', 'Charlie']
edades = [25, 30, 35]
combinados = zip(nombres, edades)
for nombre, edad in combinados:
    print(nombre, edad)  # Salida: Alice 25, Bob 30, Charlie 35
```
```python
# Combinar tres listas
ciudades = ['New York', 'Los Angeles', 'Chicago']
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(nombre, edad, ciudad)  # Salida: Alice 25 New York, Bob 30 Los Angeles, Charlie 35 Chicago
```
### 3. Funciones de manipulacion de cadenas
Una función de manipulación de cadenas es una función dentro de un programa informático diseñada específicamente para operar y transformar cadenas de caracteres.

son métodos integrados en Python que se utilizan para manipular y manejar cadenas de texto.
#### Funcion format():
En Python, `format()` es un método que se utiliza para `formatear cadenas` de texto de manera más flexible y legible. Este método permite insertar valores variables dentro de una cadena de formato, facilitando la creación de cadenas compuestas por texto fijo y valores dinámicos.
>EJEMPLO
```python
# Usando argumentos posicionales
mi_cadena = "Hola, {}. Tienes {} años."
resultado = mi_cadena.format("Alice", 30)
print(resultado)  # Salida: Hola, Alice. Tienes 30 años.
```
#### Funcion split():
En python, la funcion `split()` se utiliza para `dividir una cadena` en subcadenas basadas en un delimitador especificado.
>EJEMPLO
```python
# Dividir por espacios en blanco
mi_cadena = "Hola mundo"
resultado = mi_cadena.split()
print(resultado)  # Salida: ['Hola', 'mundo']
```
```python
# Limitar el número de divisiones
mi_cadena = "uno:dos:tres:cuatro"
resultado = mi_cadena.split(':', maxsplit=2)
print(resultado)  # Salida: ['uno', 'dos', 'tres:cuatro']
```
#### Funcion join():
En python la funcion `join()` se utliza para `unir elementos de una lista` (u otro iterable) en una cadena, con un delimitador específico entre cada elemento.
>EJEMPLO
```python
# Unir una lista de cadenas con un espacio
mi_lista = ['Hola', 'mundo']
resultado = ' '.join(mi_lista)
print(resultado)  # Salida: Hola mundo
```
```python
# Unir una lista de cadenas con una coma
mi_lista = ['uno', 'dos', 'tres']
resultado = ','.join(mi_lista)
print(resultado)  # Salida: uno,dos,tres
```
### 4. Funciones de control de flujo:

- `print()` para imprimir resultados por consola.
- `input()` para recibir datos del usuario.
  
## Tipod de funciones
### Funciones anonimas (Funciones lambda)
una funcion que no tiene nombre 
```python
lambda:"hola"
# normal
def saludo():
    return "hola"
```
### Funciones closure
son funciones que dentro de su cuerpo tiene otra funcion
### Funciones callback
son funciones que recibe por parametro otra funcion

### Programacion funcional
la programacion funcional no requiere que sepas como se deasarrola y ejecuta el procesamiento de la informacion

**ejemplo**
```python
# programacion iterativa
lista=[5,7,4,8,1]
def num_min(l):
    for i in l:
        if n < minimo:
            minimo=n
    return minimo
```
```python
# programacion funcional
min(lista)
```
#### TAREA SOBRE MAP(), FILTER(), REDUCE()
**map():**

La función `map()` en Python es una función integrada que permite aplicar una función especificada a cada elemento de un iterable (como una lista, tupla, etc.) y devolver un nuevo iterable con los resultados.
>Ejemplos
```python
# Usar map() con una función definida:

def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
resultado = map(cuadrado, numeros)
print(list(resultado))  # [1, 4, 9, 16, 25]
```
```python
# Usar map() con una función lambda:

numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x ** 2, numeros)
print(list(resultado))  # [1, 4, 9, 16, 25]
```
**filter():**

La función `filter()`, es quizás, una de las funciones más utilizadas al momento de trabajar con colecciones. Cómo su nombre lo indica, esta función nos permite realizar un filtro sobre los elementos de la colección.

La función `filter` también recibe una función y una lista pero el resultado es la lista inicial filtrada. Es decir, se pasa cada elemento de la lista por la función, y sólo si su resultado es True, se incluye en la nueva lista.
>Ejemplos
```python
# Definir una función que devuelve True si un número es par
def es_par(x):
    return x % 2 == 0

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar filter para obtener solo los números pares
resultado = filter(es_par, numeros)

# Convertir el resultado a una lista y mostrarlo
print(list(resultado))
```
**reduce():**

Usaremos la función `reduce()` cuando poseamos una colección de elementos y necesitemos generar un único resultado. reduce nos permitirá reducir los elementos de la colección. Podemos ver a esta función como un acumulador.
```python
reduce(función a aplicar, objeto iterable)
```
Aquí lo importante es detallar la función a aplicar. Esta función debe de poseer, obligatoriamente, dos parámetros. El primer parámetro hará referencia al acumulador, un variable que irá modificando su valor por cada uno de los elementos en la colección. Por otro lado, el segundo parámetro hará referencia a cada elemento de la colección. La función debe de retornar un nuevo valor, será este nuevo valor el que será asignado al acumulador.

Todo esto suena algo confuzo 🤔, pero no te preocupes, veamos un par de ejemplos.
```python
#Obtener la suma de todos los elementos en la lista

lista = [1,2,3,4]
acumulador = 0;

for elemento in lista:
    acumulador += elemento

print(acumulador)
```