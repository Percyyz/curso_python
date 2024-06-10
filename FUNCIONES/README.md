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