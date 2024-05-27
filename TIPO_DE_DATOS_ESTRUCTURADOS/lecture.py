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

texto_largo="este es un texto largo chiquitas y chiquitos"
nuevo_texto=texto_largo.split(" ")
print(nuevo_texto)