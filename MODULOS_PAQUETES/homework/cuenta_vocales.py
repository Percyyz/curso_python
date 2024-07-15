"""este es el scrip principal"""
def f_cuenta_vocales(texto:str):
    """funcion para contar la cantidad de vocales a que aparece en un texto"""
    texto_minusculas:str=texto.lower()
    cantidad_volcales=0
    for n in texto_minusculas:
        if n =="a":
            cantidad_volcales+=1
    return cantidad_volcales
