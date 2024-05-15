# CONTROLES DE FLUJO
Todos los programas trabajan atraves de instrucciones ordenadas.
existen maneras de romper con el flujo normal de los programs creando
`bifurcaciones` o creando `repiticion` de instrucciones.
## DECISIONES
### LA SENTENCIA "IF"
La sentencia de decisiones en python es `if`. en su estrucctura debemos añadir una **expresion de comparacion** terminando con `:` al final de la linia
>  Ejemplo

```python
if true:
    print("es verdad")
```
`if` va ejecutar el codigo dependiendo si cumple una condicion
un flujo normal es un codigo que va linia por linia
> Ejemplo
```python
saludo="hola como estas"
nombre="jose luis"
print(saludo+nombre)
## CON IF
saludo="hola como estas"
nombre="jose luis"
if True:
     print(saludo+nombre)
#
saludo="hola como estas"
nombre="jose luis"
if True:
     print("soy verdad")
else:
     print("soy falso")
print("se ejecuta siempre")
```
## CICLOS
 son los contrloes de flujo que repiten codigo y sintaxis es la siguitente
### for
 este codigo imprime los numeros del 1 al 10
 >ejemplo
 ```python
 for n in range(1,11):
     print(n)
 ```
 ## uso de memoria es for
 `enumerate->` en palabras pequeñas hace uso mas de memoria pero cuando son textos grandes
 y medianos, almacena menos y ejecuta mas rrapido.
 `range->` para oraciones pequeñas
 `in->` para oraciones medianas es mas rrapido y consume menos.
### while


