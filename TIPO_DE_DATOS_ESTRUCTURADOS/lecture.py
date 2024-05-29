# lista=["abel","antony","rony"]
# print(lista[1])
# diccionarios={"nombre":"antonio","edad":15,"sexo":False}
# print(diccionarios["nombre"])

# ## list
# texto="hola"
# lista_texto=list(texto)
# lista2=[e for e in texto]
# print(lista2)

# ## split
# texto_largo="hola como estan bienvenidos al salon"
# nueva_lista=texto_largo.split(" ")
# print(nueva_lista)

# ####
# texto_largo="hola como estan bienvenidos al salon"
# nuevo_texto=texto_largo[16:]
# nueva_lista=nuevo_texto.split(" ")
# print(nueva_lista)

# #####
# texto_largo="loquitas_.mp4"
# nuevo_texto=texto_largo.split(".")
# print(nuevo_texto[-1])

#### .join() - se utiliza para unir elementos de una lista o convierte listas en texto
# texto_largo="loquitas_.mp4"
# nuevo_texto=texto_largo.split("_")
# print(" ".join(nuevo_texto))

# texto_largo="este es un texto largo chiquitas y chiquitos"
# nuevo_texto=texto_largo.split(" ")
# print(nuevo_texto)

# DATO estructurado
lista_original=[1,2,3,4]
copia_lista=lista_original

lista_original[-1]=15

print(copia_lista)

# copia la referencia o la direccion de una lista original

# crear un programa que reciba una lista desordenada y muestre por terminal una lista ordenada y la lista previa a ser ordenada.
lista=[6,2,8,4,7,3,1]
copia_lista=lista.copy() # copy() copia el valor de la lista
copia_lista.sort() # sort() ordena el valor de la lista 
print(lista)
print(copia_lista)

