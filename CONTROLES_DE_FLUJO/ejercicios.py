# escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor
# de edad ono.
edad_usuario=int(input("ingrese su edad :"))
if edad_usuario>=18:
    print("es mayor de edad")
else:
    print("no es mayor de edad")

## escribir un programa que almacene la cadena de caracteres contraseña en una variable
# pregunte al usuario por una contraseña y y imprima por pantalla si la contraseña introducida por el usuario 
# coincide con la guardada en la variable sin tener en cuenta mayusculas y minusculas

contraseña="yarihuaman14"
contraseña_usuario=input("ingrese una contraseña :")
if contraseña == contraseña_usuario:
    print("la contraseña es correcta")
else:
    print("la contraseña es incorrecta")

# ## escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla
# # la cuenta de atras desde ese numero asta cero separados por comas 

numero=int(input("ingrese un numero entero positivo "))
resultado=""
for i in range(numero, -1, -1):
    resultado+=str(i)
    if i >0:
        resultado+=","
print(resultado)

# crear un programa que me muestre la tabla de multiplicar de 1 asta 5
for i in range(1,6):
    for n in range(1,13):
        print(f"{i}x{n}={i*n}")

# crear un programa que pida un numero y que muestre la tabla de multiplicar de ese numero
numero:int = int(input("Introduce un número: "))
for i in range(1, 13):
    print(f"{numero} x {i} = {numero*i}")