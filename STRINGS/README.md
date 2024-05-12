# OPERADORES PARA ESTRING - TEXTO
Los operadores para manipular y trabajar con cadenas de texto `strings` 
varían según el lenguaje de programación que estés utilizando

>Ejemplo
```python
vocales="aeiou"
#        01234     indices positivos
#      -5-4-3-2-1  indices negativos
print(len(vocales))
print(vocales[3])
print(vocales[-2])
print(vocales[:]) #: es operador de corte
print(vocales[3:])
```
cuando tengo el signo (+) entre dos textos "hola"+"mundo" es operador de concatenacion.
> Ejemplo
```python
"Hola" + " mundo" => "Hola mundo"
```
Esta función o método se utiliza para obtener la longitud (número de caracteres) de 
una cadena de texto y podemos utilizar una sintxis similar `length` o `len`.
> Ejemplo
```python
len("Hola mundo") => 11
```