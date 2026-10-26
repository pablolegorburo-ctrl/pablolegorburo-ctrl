def contar_vocales(palabra):    
    vocales = "aeiou"
    contador = 0

    for caracter in palabra.lower():
        if caracter in vocales:
            contador += 1
    return contador


print(contar_vocales("legoooooor"))

    