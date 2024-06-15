def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(f'{clave}: {valor}')

# Llamada a la función con argumentos nominales empaquetados
imprimir_datos(nombre='Ana', edad=28, ciudad='Barcelona')