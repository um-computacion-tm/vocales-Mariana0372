


def obtener_vocales(frase):
    vocales = "AEIOU"

    return set([c for c in frase if c in vocales])
    

texto = input("ingresa una frase: ")

print(obtener_vocales(frase))
print(len(obtener_vocales(texto)))
