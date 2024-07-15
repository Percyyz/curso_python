"""este es el scrip principal"""
def f_es_menor(lista:list):
    """funcion para saber el numero meñor de una lista"""
    menor=lista[0]
    for n in lista:
        if n< menor:
            menor=n
    return menor
