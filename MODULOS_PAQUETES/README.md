# averiguar modulos y paquetes en python
**modulo:** 

Es un conjunto de funciones o un achivo `.py` con funciones

Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar grandes códigos.

Consideremos, por ejemplo, un archivo `aritmetica.py` que contenga las siguientes definiciones.

>EJEMPLO:
```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b
```
Podemos acceder a ellas desde otro archivo de Python ubicado en la misma ruta importando el módulo.

```python
import aritmetica

print(aritmetica.sumar(7, 5))
```
Una sintaxis alternativa para importar objetos desde un módulo es la siguiente.
```python
from aritmetica import sumar

print(sumar(7, 5))
```
Nótese que, en este segundo caso, no se prefija el nombre del módulo al invocar al objeto importado. Podemos importar varios objetos separándolos por comas.
```python
from aritmetica import sumar, restar, mult, div

print(sumar(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))
```
O bien, para importar todos los objetos dentro de un módulo:
```python
from aritmetica import *
```

**paquete:** 

es una carpeta con una serie de archivos `.py`.

Un paquete es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.

```python
matematica/

    |-- __init__.py

    |-- aritmetica.py

    |-- geometria.py
```

Debe contener siempre un archivo `__init__.py` (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.
```python
import matematica.aritmetica
print(matematica.aritmetica.sumar(7, 5))
```
O bien de la siguiente.
```python
from matematica import aritmetica
print(aritmetica.sumar(7, 5))
```
También, esta otra:
```python
from matematica.aritmetica import sumar
print(sumar(7, 5))
```
# diferencias entre modulos y paquetes

 Los módulos son archivos individuales de Python, mientras que los paquetes son directorios que contienen múltiples módulos organizados de manera jerárquica.

**MODULO**
>Ejemplo
```python
# mi_modulo.py
def hola():
    print("Hola desde el módulo")
```
>Uso:
```python
import mi_modulo
mi_modulo.hola()
```
**PAQUETE**

Estructura de directorios:
```python
mi_paquete/
    __init__.py
    modulo1.py
    subpaquete/
        __init__.py
        modulo2.py
```
Contenido de modulo1.py:
```python
def funcion1():
    print("Función 1 en módulo 1")
```
Contenido de subpaquete/modulo2.py:
```python
def funcion2():
    print("Función 2 en módulo 2")
```
>Uso:

```python
import mi_paquete.modulo1
import mi_paquete.subpaquete.modulo2

mi_paquete.modulo1.funcion1()
mi_paquete.subpaquete.modulo2.funcion2()
```